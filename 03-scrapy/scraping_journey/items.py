# ============================================
# 📄 items.py — Veri Modeli (Item) Tanımı
# ============================================
#
# Bu dosya, Scrapy'nin toplayacağı verilerin yapısını tanımlar.
# Yani her bir "quote" (alıntı) için hangi bilgilerin
# kaydedileceğini burada belirleriz.
#
# Scrapy'de her veri tipi bir "Item" sınıfı ile temsil edilir.
# Her alan (Field), CSV veya JSON çıktısında bir sütun olur.
# ============================================


# Scrapy kütüphanesini içe aktarır
import scrapy


# ============================================
# 🧱 ScrapingJourneyItem Sınıfı
# ============================================
#
# Bu sınıf, her bir alıntının sahip olacağı alanları (field)
# tanımlar. Bu alanlar pipeline, spider ve output dosyaları
# arasında veri taşımada kullanılır.
# ============================================

class ScrapingJourneyItem(scrapy.Item):
    # Alıntının (quote) metin içeriği
    text = scrapy.Field()

    # Alıntıyı söyleyen kişinin adı
    author = scrapy.Field()

    # Alıntıya ait etiketler (birden fazla olabilir)
    tags = scrapy.Field()

    # Alıntının bulunduğu sayfanın URL adresi
    source_url = scrapy.Field()
