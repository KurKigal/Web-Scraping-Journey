# 🕷️ Web Scraping'e Giriş

## Web Scraping Nedir?

Web scraping, web sitelerinden otomatik olarak veri çekme işlemidir. İnsanların manuel olarak yaptığı işlemi (web sitesine girme, bilgileri okuma, kopyalama) bilgisayarın otomatik yapmasını sağlarız.

### Basit Bir Analoji
İnternetteki web siteleri büyük bir kütüphane gibidir. Web scraping ise bu kütüphanede:
- Belirli konulardaki kitapları bulma
- İhtiyacınız olan sayfaları fotokopi çekme  
- Bu bilgileri düzenli bir şekilde arşivleme

işlemidir.

## 🎯 Nerelerde Kullanılır?

### 1. E-ticaret
```
Örnekler:
- Rakip firmaların fiyatlarını takip etme
- Ürün stoklarını kontrol etme  
- Müşteri yorumlarını analiz etme
```

### 2. Haber ve İçerik Toplama
```
Örnekler:
- Günlük haber başlıklarını toplama
- Blog yazılarını analiz etme
- Sosyal medya trendlerini takip etme
```

### 3. Araştırma ve Akademik Çalışmalar
```
Örnekler:
- İstatistiksel veri toplama
- Pazar araştırması yapma
- Bilimsel makaleleri indeksleme
```

### 4. Finans ve Borsa
```
Örnekler:
- Hisse senedi fiyatlarını takip etme
- Kripto para verilerini toplama
- Ekonomik göstergeleri analiz etme
```

## 🛠️ Web Scraping Süreci

### Adım 1: Web Sitesini Analiz Etme
```
- Hangi veriyi istiyoruz?
- Veri hangi HTML elementlerinde?
- Site JavaScript kullanıyor mu?
- Anti-scraping önlemleri var mı?
```

### Adım 2: Araç Seçimi
```
Basit HTML → Requests + BeautifulSoup
Karmaşık siteler → Scrapy
JavaScript ağır → Selenium/Playwright
Büyük veri → Scrapy + asenkron işlem
```

### Adım 3: Kod Yazma
```python
# Temel yapı her zaman şu şekilde:
1. HTTP isteği gönder
2. HTML içeriğini al
3. HTML'i parse et
4. İstenen veriyi çıkar
5. Veriyi kaydet
```

### Adım 4: Test ve Optimizasyon
```
- Kodun düzgün çalışıp çalışmadığını test et
- Hız optimizasyonu yap
- Hata durumlarını yönet
```

## 🔍 HTML Temelleri (Hızlı Hatırlatma)

Web scraping için HTML'in temellerini bilmek şart:

### HTML Tag'ları
```html
<div class="product">           <!-- Container -->
    <h2 class="title">Ürün Adı</h2>      <!-- Başlık -->
    <span class="price">100 TL</span>     <!-- Fiyat -->
    <p id="description">Açıklama...</p>   <!-- Açıklama -->
</div>
```

### CSS Selector'ları
```css
.product        → class="product" olan elementler
#description    → id="description" olan element  
h2.title        → h2 tag'i ve class="title" olan
div > span      → div'in doğrudan alt elemanı olan span
```

## 🚀 İlk Adımlarınız

1. **Python temellerinizi gözden geçirin**
2. **HTML/CSS temellerini hatırlayın**  
3. **Developer tools'u öğrenin (F12)**
4. **Bu repo'daki örnekleri sırasıyla çalışın**

## 🎯 Öğrenme Yolu

```
Seviye 1: requests + BeautifulSoup
    ↓
Seviye 2: Scrapy framework  
    ↓
Seviye 3: JavaScript rendering
    ↓
Seviye 4: Büyük ölçekli projeler
    ↓
Seviye 5: Anti-scraping bypass
```

## 💡 İpuçları

- **Küçük başlayın**: İlk projede Amazon'u scraping yapmaya çalışmayın
- **Developer tools kullanın**: F12'ye basıp siteleri inceleyin
- **Etik olun**: Sitelere zarar vermeyin
- **Test edin**: Kodunuzu farklı sayfalarda test edin

Sonraki adım: `ethics.md` dosyasını okuyun ve etik kuralları öğrenin!
