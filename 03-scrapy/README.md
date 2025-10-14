# 🕷️ 03-Scrapy — Yapılandırılmış Web Scraping Girişi

Bu bölümde, Python’un **Scrapy** çatısını kullanarak veri çekmeyi öğreneceğiz.  
Scrapy, *Requests + BeautifulSoup* gibi manuel yöntemlere göre çok daha güçlü bir sistem sağlar.  
Otomatik sayfa geçişi, CSV/JSON çıktı yönetimi, pipeline ve middleware gibi gelişmiş özellikler sunar.

---

## 📚 Hedef Site

> [https://quotes.toscrape.com](https://quotes.toscrape.com)

Bu site, web scraping denemeleri için özel olarak hazırlanmıştır.  
Her sayfada 10 adet alıntı (quote) bulunur ve “Next” butonuyla sonraki sayfaya geçilir.

Örnek HTML yapısı:

```html
<div class="quote">
  <span class="text">“The world as we have created it...”</span>
  <span>by <small class="author">Albert Einstein</small></span>
  <div class="tags">
    <a class="tag">change</a>
    <a class="tag">thinking</a>
  </div>
</div>
```

---

## 🧩 Proje Yapısı

```
03-scrapy/
│
├── scraping_journey/
│   ├── __init__.py
│   ├── items.py                # Veri modelinin tanımı
│   ├── middlewares.py          # Spider ve Downloader ara katmanları
│   ├── pipelines.py            # Veri işleme aşamaları (temizleme, kayıt)
│   ├── settings.py             # Scrapy yapılandırması (User-Agent, delay vb.)
│   └── spiders/
│       ├── __init__.py
│       └── basic_spider.py     # Asıl veri çekme mantığı (quotes crawler)
│
├── output/                     # CSV çıktı dosyalarının kaydedileceği klasör
└── README.md
```

---

## ⚙️ Çalıştırma Adımları

### 1️⃣ Ortamı Aktifleştir
```bash
conda activate wsc
```

### 2️⃣ Proje Klasörüne Gir
```bash
cd 03-scrapy
```

### 3️⃣ Spider’ı Çalıştır
```bash
scrapy crawl quotes
```

> Bu komut, `basic_spider.py` dosyasındaki `QuotesSpider` sınıfını çalıştırır.  
> Tüm sayfalardaki alıntılar otomatik olarak gezilir ve `output/quotes.csv` dosyasına kaydedilir.

---

## 📦 Çıktı Örneği

`output/quotes.csv` dosyası aşağıdaki gibi görünür:

| author | source_url | tags | text |
|------|---------|------|-------------|
| Albert Einstein | https://quotes.toscrape.com/ | change, deep-thoughts, thinking, world | “The world as we have created it...” |
| J.K. Rowling | https://quotes.toscrape.com/page/1/ | abilities, choices | “It is our choices, Harry…” |

---

## 🧱 Ekstra Bilgi

- 📘 [Scrapy Dokümantasyonu](https://docs.scrapy.org/en/latest/)
- 🧠 [XPath vs CSS Seçicileri](https://docs.scrapy.org/en/latest/topics/selectors.html)
- ⚖️ **Etik Scraping:** `ROBOTSTXT_OBEY = True` ayarı sayesinde sitelerin izin verdiği sayfalar dışında veri çekilmez.

---

## ✨ Özet

Bu bölüm, “Requests + BeautifulSoup” aşamasını tamamlamış geliştiriciler için bir sonraki adımdır.  
Scrapy, daha büyük projelerde, **yapılandırılmış, ölçeklenebilir ve yeniden kullanılabilir** scraping işlemleri yapmak isteyenler için ideal bir temeldir.

---

> 🔗 *Bu repo eğitim amaçlıdır. Gerçek web sitelerinde scraping yapmadan önce izin alınması gerekir.*
