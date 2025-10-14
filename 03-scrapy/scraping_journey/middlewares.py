# ============================================
# 🧩 middlewares.py — Middleware (Ara Katmanlar)
# ============================================
#
# Scrapy, veriyi işlerken "katmanlı" bir sistem kullanır.
# Bu katmanlara MIDDLEWARE denir.
#
# İki tür middleware vardır:
#   1️⃣ Spider Middleware — Spider’a gelen ve çıkan veriyi yönetir
#   2️⃣ Downloader Middleware — HTTP istek ve yanıtlarını kontrol eder
#
# Middleware’lar sayesinde:
#   - Ek header eklenebilir
#   - Proxy veya User-Agent ayarlanabilir
#   - Hatalar yakalanabilir
#   - Log veya özel filtreleme yapılabilir
# ============================================

from scrapy import signals

# ItemAdapter, item tiplerini tek bir arayüzle yönetmek için kullanılır
from itemadapter import ItemAdapter


# ============================================
# 🕷️ 1️⃣ ScrapingJourneySpiderMiddleware
# ============================================
#
# Bu sınıf, Spider ile Response nesneleri arasındaki trafiği yönetir.
# Yani sayfa içeriği spider’a gönderilmeden önce veya
# spider çıktı ürettikten sonra devreye girer.
# ============================================

class ScrapingJourneySpiderMiddleware:
    # Not: Scrapy’de tüm metodları tanımlamak zorunlu değildir.
    # Tanımlanmayan metodlar varsayılan davranışla çalışır.

    @classmethod
    def from_crawler(cls, crawler):
        """
        Scrapy, middleware’ları bu metot aracılığıyla oluşturur.
        Ayrıca burada sinyallere (signals) bağlanabiliriz.
        """
        s = cls()
        # Spider açıldığında "spider_opened" sinyali tetiklenir
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        Her response, spider’a iletilmeden hemen önce çağrılır.
        Burada response üzerinde değişiklik yapabiliriz.
        """
        # None dönerse işlem normal devam eder.
        return None

    def process_spider_output(self, response, result, spider):
        """
        Spider bir response’u işledikten sonra çağrılır.
        Burada spider’dan çıkan item veya request’leri değiştirebiliriz.
        """
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        Spider veya bu middleware hata fırlatırsa devreye girer.
        Hata loglama veya kurtarma işlemleri burada yapılabilir.
        """
        pass

    async def process_start(self, start):
        """
        (Nadiren kullanılır)
        Asenkron spider başlangıç işlemleri için kullanılır.
        """
        async for item_or_request in start:
            yield item_or_request

    def spider_opened(self, spider):
        """
        Spider ilk kez başlatıldığında çağrılır.
        Loglama veya başlangıç mesajı göstermek için uygundur.
        """
        spider.logger.info(f"🕷️ Spider başlatıldı: {spider.name}")


# ============================================
# ⚙️ 2️⃣ ScrapingJourneyDownloaderMiddleware
# ============================================
#
# Downloader middleware, en alt katmanda çalışır.
# Görevi:
#   - HTTP istekleri gönderilmeden önce müdahale etmek
#   - Yanıtlar alındığında işlemek
#   - Gerekirse proxy, header, cookie eklemek
# ============================================

class ScrapingJourneyDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        """
        Scrapy bu metodu kullanarak downloader middleware’i başlatır.
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        Her HTTP isteği gönderilmeden önce çağrılır.
        Burada:
          - Header eklenebilir
          - Proxy ayarlanabilir
          - İstek iptal edilebilir
        """
        # None dönerse Scrapy isteği normal şekilde devam ettirir.
        return None

    def process_response(self, request, response, spider):
        """
        Downloader’dan dönen her yanıt burada yakalanır.
        Yanıt üzerinde değişiklik yapabilir, gerekirse
        yeni bir istek oluşturabiliriz.
        """
        # Response’ı değiştirmeden olduğu gibi döndürür.
        return response

    def process_exception(self, request, exception, spider):
        """
        Bir istek sırasında hata oluşursa burası çağrılır.
        Burada alternatif işlem veya yeniden deneme yapılabilir.
        """
        pass

    def spider_opened(self, spider):
        """
        Spider açıldığında bilgi loglamak için kullanılır.
        """
        spider.logger.info(f"🚀 Downloader aktif: {spider.name}")
