# Scrapy settings for splash_project

BOT_NAME = "splash_project"
SPIDER_MODULES = ["splash_project.spiders"]
NEWSPIDER_MODULE = "splash_project.spiders"

# ==============================================================================
# 🌊 SPLASH ENTEGRASYON AYARLARI
# ==============================================================================

# 1. Splash Sunucu Adresi (Docker'da çalışan adres)
SPLASH_URL = 'http://localhost:8050'

# 2. Splash Middleware'lerini Aktif Etme
DOWNLOADER_MIDDLEWARES = {
    # Varsayılan Scrapy middleware'leri
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# 3. Spider Middleware (Splash argümanlarını işlemek için)
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# 4. Duplicate Filter (Splash argümanlarına göre filtreleme yapmak için özel sınıf)
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# 5. Cache Storage (İsteğe bağlı, cache kullanacaksanız Splash uyumlu olmalı)
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# ==============================================================================
# 🛡️ ETİK AYARLAR
# ==============================================================================
ROBOTSTXT_OBEY = False  # Eğitim sitelerinde bazen sorun çıkarabilir, şimdilik False
DOWNLOAD_DELAY = 1      # JS render işlemi sunucuyu yorar, nazik olalım

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"