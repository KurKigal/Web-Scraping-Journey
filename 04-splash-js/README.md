# ⚡ JavaScript Rendering ve Splash

## 🤔 Sorun: "Veri Nerede?"

Bugüne kadar `requests` veya standart `Scrapy` ile sitelere istek attık. Sunucu bize bir HTML döndü ve biz de içinden veriyi ayıkladık.

Ancak modern web siteleri (React, Vue, Angular ile yazılanlar) farklı çalışır:
1. Siteye girersiniz, size **boş bir HTML** gelir.
2. Tarayıcınız JavaScript kodlarını indirir ve çalıştırır.
3. JavaScript, veriyi sunucudan (API) çeker ve sayfaya yerleştirir.

Standart Scrapy JavaScript çalıştıramaz. Bu yüzden sayfayı **boş** görür.

## 🛠️ Çözüm: Headless Browsers

Bu sorunu çözmek için bir "tarayıcı" gibi davranan araçlara ihtiyacımız var.

### Neden Splash?
- **Hafif:** Chrome/Firefox kadar kaynak tüketmez.
- **Scrapy Entegrasyonu:** `scrapy-splash` ile Scrapy içinde doğal bir parça gibi çalışır.
- **Programlanabilir:** Lua scriptleri ile "Tıkla", "Kaydır", "Bekle" komutları verilebilir.

*(Not: Alternatif olarak Selenium veya Playwright da kullanılır, ancak Scrapy ekosisteminde Splash hala popülerdir.)*

## 🚀 Neler Öğreneceğiz?
1. Docker üzerinde Splash servisi kaldırmayı
2. Scrapy projesini Splash'e bağlamayı
3. Dinamik (JS ile yüklenen) siteleri scrape etmeyi
4. Lua scriptleri ile sayfada işlem yapmayı