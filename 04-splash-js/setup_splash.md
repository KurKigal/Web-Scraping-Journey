# 🐳 Splash Kurulumu (Docker)

Splash, Python kütüphanesi olarak değil, bir **servis** (Docker container) olarak çalışır. Scrapy bu servise istek atar, Splash sayfayı render eder ve sonucu Scrapy'ye döndürür.

## Adım 1: Docker Kurulumu
Eğer bilgisayarınızda Docker yoksa [Docker Desktop](https://www.docker.com/products/docker-desktop) uygulamasını indirip kurun.

## Adım 2: Splash'i Çalıştırma
Terminal veya CMD'yi açın ve şu komutu girin:

```bash
docker run -p 8050:8050 scrapinghub/splash
```

Bu komut:

1. Splash imajını indirir (yaklaşık 1 GB).
    
2. 8050 portunda bir sunucu başlatır.
    

## Adım 3: Kontrol

Tarayıcınızda `http://localhost:8050` adresine gidin. Eğer Splash logosunu ve bir arama kutusunu görüyorsanız kurulum tamamdır! 🎉

## Adım 4: Python Paketleri

Proje klasöründe gerekli paketi kurun:

```bash
pip install scrapy-splash
```
