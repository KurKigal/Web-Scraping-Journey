# ============================================
# 📦 pipelines.py — Veriyi İşleme (Pipeline) Katmanı
# ============================================
#
# Scrapy’de toplanan her item (veri), spider’dan çıktıktan sonra
# "pipeline" adı verilen aşamalardan geçer.
#
# Bu dosyada veriler:
#   - temizlenebilir (örnek: boşlukları silmek)
#   - doğrulanabilir (örnek: eksik alanları kontrol etmek)
#   - kaydedilebilir (örnek: veritabanına veya dosyaya)
#
# Şu anda bu pipeline basit tutulmuştur.
# Öğrenme aşamasında verileri doğrudan geri döndürür.
# ============================================


# Scrapy item’larını kolayca işleyebilmek için kullanılan yardımcı sınıf
from itemadapter import ItemAdapter


# ============================================
# 🧩 ScrapingJourneyPipeline Sınıfı
# ============================================
#
# Scrapy, toplanan her veriyi (item’ı) bu sınıftan geçirir.
# Eğer ayarlarda aktif edilirse, bu sınıf `process_item()` metodunu
# her item için otomatik olarak çağırır.
# ============================================

class ScrapingJourneyPipeline:
    # Her yeni item geldiğinde Scrapy bu fonksiyonu çalıştırır.
    def process_item(self, item, spider):
        # "item" → spider’dan gelen veri
        # "spider" → bu veriyi toplayan spider nesnesi

        # Şu anda veriyi olduğu gibi (hiç değiştirmeden) geri döndürüyoruz.
        # İleri seviye projelerde burada:
        #   - veritabanına kayıt
        #   - veri temizleme
        #   - dosya yazımı işlemleri yapılabilir.
        return item
