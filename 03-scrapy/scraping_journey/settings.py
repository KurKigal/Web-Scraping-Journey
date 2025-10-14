# ============================================
# ⚙️ settings.py — Scrapy Proje Ayarları
# ============================================
#
# Bu dosya, Scrapy’nin genel çalışma davranışını tanımlar.
# Burada; istek sıklığı, etik kurallar, çıktı formatı, loglama
# gibi ayarlar yapılır.
#
# Scrapy’de ayarlar iki seviyede yapılabilir:
#   1️⃣ Global (burada)
#   2️⃣ Spider özelinde (custom_settings)
# ============================================


# --- Scrapy projesinin adı ---
BOT_NAME = "scraping_journey"


# --- Spider klasörlerinin yolları ---
SPIDER_MODULES = ["scraping_journey.spiders"]
NEWSPIDER_MODULE = "scraping_journey.spiders"


# --- Şu anda aktif eklenti yok ---
ADDONS = {}


# ============================================
# 🧭 Etik Scraping Ayarları
# ============================================
#
# Scrapy, web sitelerine aşırı yüklenmemek için
# "robots.txt" kurallarına uymayı ve isteklere gecikme
# koymayı destekler. Bu ayarlar, bot’un insan gibi davranmasını sağlar.
# ============================================

# Tarayıcı kimliği (User-Agent)
# Web sitesi tarafından bot olarak algılanmamak için tarayıcı bilgisi eklenir.
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ScrapyQuotesBot/1.0"

# Web sitelerinin robots.txt kurallarına uy (etik scraping)
ROBOTSTXT_OBEY = True


# ============================================
# ⚡ Performans ve İstek Kontrolü
# ============================================
#
# Scrapy aynı anda birden fazla isteği paralel yollayabilir.
# Ancak eğitim ve test ortamlarında, siteyi yormamak için
# istek sayısını düşürüp, her isteğe gecikme ekliyoruz.
# ============================================

# Toplam eşzamanlı istek sayısını sınırlamak (varsayılan: 16)
# CONCURRENT_REQUESTS = 16

# Aynı domaine gönderilecek maksimum istek sayısı
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Her istek arasında bekleme süresi (saniye)
DOWNLOAD_DELAY = 1


# ============================================
# 🍪 Diğer Ayarlar (isteğe bağlı)
# ============================================
#
# Buradaki satırlar, deneysel veya proje büyüdüğünde
# aktif edilebilecek ayarlardır.
# Şu anda devre dışı bırakılmıştır (yorum satırı).
# ============================================

# COOKIES_ENABLED = False
# TELNETCONSOLE_ENABLED = False


# ============================================
# 🧩 Header, Middleware, Pipeline, Extensions
# ============================================
#
# Bu bölümler gelişmiş projelerde kullanılır.
# Şu anda devre dışı, ancak Scrapy’nin dokümantasyonu
# üzerinden detayları incelenebilir.
# ============================================

# DEFAULT_REQUEST_HEADERS = {...}
# SPIDER_MIDDLEWARES = {...}
# DOWNLOADER_MIDDLEWARES = {...}
# EXTENSIONS = {...}
# ITEM_PIPELINES = {...}


# ============================================
# 🕒 AutoThrottle (isteğe bağlı hız kontrolü)
# ============================================
#
# Eğer hedef sunucu yavaşsa, Scrapy istek hızını otomatik düşürebilir.
# Bu özellikle büyük veri çekimlerinde faydalıdır.
# Şu anda devre dışı.
# ============================================

# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False


# ============================================
# 🧱 HTTP Cache (isteğe bağlı)
# ============================================
#
# Scrapy, aynı sayfaya yapılan istekleri cache’leyerek
# hız kazandırabilir. Şu anda devre dışı.
# ============================================

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"


# ============================================
# 📦 Çıktı ve Loglama
# ============================================
#
# CSV ve JSON çıktılarında Türkçe karakter desteği için
# UTF-8 kullanılır. Log seviyesi ise INFO’dur.
# ============================================

# Çıktı dosyalarının karakter kodlaması
FEED_EXPORT_ENCODING = "utf-8"

# Log ayrıntı seviyesi (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL = "INFO"


# ============================================
# 🗂️ Klasör Oluşturma
# ============================================
#
# Çıktı dosyalarının kaydedileceği klasörü (output/)
# otomatik olarak oluşturur.
# ============================================

import os
os.makedirs("output", exist_ok=True)
