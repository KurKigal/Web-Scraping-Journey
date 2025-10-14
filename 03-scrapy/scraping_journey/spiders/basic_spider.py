# ============================================
# 📄 basic_spider.py — Scrapy ile Alıntı (Quotes) Toplama
# ============================================
#
# Bu örnek, Scrapy çatısını kullanarak bir web sitesinden veri çekmenin
# temel mantığını öğretir. Hedefimiz: https://quotes.toscrape.com/
#
# Scrapy’nin `Spider` sınıfı kullanılarak:
#   - Sayfadaki her alıntıyı (quote) bulacağız
#   - Yazar isimlerini ve etiketleri çekeceğiz
#   - “Next” butonuna tıklayarak tüm sayfaları gezeceğiz
#   - Sonuçları CSV dosyasına kaydedeceğiz
# ============================================


# Scrapy modülünü içe aktarır
import scrapy

# Kendi tanımladığımız veri modelini (Item) içe aktarır
from scraping_journey.items import ScrapingJourneyItem


# ============================================
# 🕷️ QuotesSpider — Ana Spider Sınıfı
# ============================================
#
# Her Scrapy projesinde en az bir “spider” sınıfı bulunur.
# Bu sınıf, hangi siteyi ziyaret edeceğimizi, hangi verileri
# toplayacağımızı ve nasıl ilerleyeceğimizi tanımlar.
# ============================================

class QuotesSpider(scrapy.Spider):
    # Spider’ın benzersiz adı — terminalde bu isimle çağırılır
    name = "quotes"

    # Hangi domain(ler)e erişilebileceğini belirler (güvenlik için)
    allowed_domains = ["quotes.toscrape.com"]

    # Başlangıç URL’leri (Scrapy buradan başlayarak gezinir)
    start_urls = ["https://quotes.toscrape.com/"]

    # ============================================
    # 🧩 Özel Ayarlar (custom_settings)
    # ============================================
    #
    # Her spider kendi özel ayarlarını tanımlayabilir.
    # Burada yaptıklarımız:
    #   1️⃣ Çıktıyı CSV olarak kaydetmek
    #   2️⃣ Gereksiz yüklenmeyi önlemek için istekler arası gecikme koymak
    # ============================================

    custom_settings = {
        # Çıktıyı CSV olarak kaydet
        "FEEDS": {
            "output/quotes.csv": {
                "format": "csv",        # CSV formatında kayıt
                "overwrite": True,      # Her çalıştırmada dosyayı sıfırla
                "encoding": "utf8"      # Türkçe karakter uyumu
            }
        },
        # İstekler arası bekleme (etik scraping)
        "DOWNLOAD_DELAY": 1.0,
    }


    # ============================================
    # 🔍 parse() — Ana Fonksiyon
    # ============================================
    #
    # Bu fonksiyon, her sayfa yüklendiğinde otomatik olarak çağrılır.
    # `response` parametresi, o sayfanın HTML içeriğini temsil eder.
    # ============================================

    def parse(self, response):
        """Her sayfada çağrılan ana fonksiyon."""
        
        # --- Her bir quote bloğunu seç ---
        # Sayfadaki tüm <div class="quote"> elemanlarını bulur.
        # Her bir quote bloğunda metin, yazar ve etiket bilgileri vardır.
        for quote in response.css("div.quote"):
            # Tanımladığımız Item sınıfını kullanarak boş bir veri nesnesi oluşturur
            item = ScrapingJourneyItem()

            # Alıntı metnini <span class="text"> içinden alır
            item["text"] = quote.css("span.text::text").get()

            # Yazar adını <small class="author"> içinden alır
            item["author"] = quote.css("small.author::text").get()

            # Etiketleri (tag'leri) <a class="tag"> içinden liste olarak alır
            item["tags"] = quote.css("div.tags a.tag::text").getall()

            # Verinin alındığı sayfa adresini kaydeder
            item["source_url"] = response.url

            # Toplanan veriyi Scrapy motoruna teslim eder
            yield item


        # ============================================
        # 🔁 Sayfa Geçişi — “Next” Butonu
        # ============================================
        #
        # Scrapy’de sayfalar arası geçiş (pagination) bu şekilde yapılır.
        # “Next” butonunun bağlantısını alır, varsa sonraki sayfayı ziyaret eder.
        # ============================================

        # --- Sayfa geçişi (Next butonu) ---
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            # relative URL → absolute URL’ye dönüştürülür
            # (örnek: "/page/2/" → "https://quotes.toscrape.com/page/2/")
            yield response.follow(next_page, callback=self.parse)
