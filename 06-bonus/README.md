# 🛡️ Bonus: Anti-Ban ve Yüksek Performans

Tebrikler! Web scraping yolculuğunun sonuna geldiniz. Bu bölümde artık "Junior" seviyesinden çıkıp "Pro" seviyesine geçiş için gereken teknikleri inceliyoruz.

## 🎯 Bu Bölümde Neler Var?

### 1. Anti-Ban Teknikleri (Banlanmamak İçin)
Web siteleri botları engellemek için IP adreslerini veya User-Agent (tarayıcı kimliği) bilgilerini kontrol eder.
- **Proxy Rotasyonu:** Her istekte farklı bir IP adresi kullanmak.
- **User-Agent Rotasyonu:** Her istekte farklı bir tarayıcı (Chrome, Firefox, Safari) gibi davranmak.

### 2. Asenkron Scraping (Hız Canavarı)
Standart `requests` kütüphanesi **senkrondur**. Yani bir sayfayı indirirken diğer işlemleri bloklar (bekletir). 
**Asenkron (Async)** scraping ise aynı anda yüzlerce sayfayı indirebilir.

## 🛠️ Kurulum

```bash
pip install -r requirements.txt
```

## 📂 Dosyalar

### `proxy_manager.py`

Bu script, `fake-useragent` kütüphanesini kullanarak her istekte kimliğinizi değiştirir ve proxy kullanım mantığını gösterir.

### `async_scraping.ipynb`

Bu notebook'ta `requests` (yavaş) ile `aiohttp` (hızlı) kütüphanelerini yarıştırıyoruz. Aradaki hız farkına inanamayacaksınız!