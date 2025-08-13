# ⚖️ Web Scraping Etiği ve Yasal Konular

## 🎯 Neden Etik Önemli?

Web scraping güçlü bir araç ama **büyük güç, büyük sorumluluk getirir**. Yanlış kullanım:
- Web sitelerini çökertebilir
- Yasal sorunlara yol açabilir  
- İş kaybına sebep olabilir
- Etik olmayan veri kullanımına neden olabilir

## 📜 Temel Etik İlkeler

### 1. **"İyi Komşu" Prensibi**
```
Soru: Bu web sitesinin sahibi olsaydım, 
      böyle scraping yapılmasına razı olur muydum?

✅ Makul hızda, makul sayıda istek
❌ Siteyi çökertirecek kadar yoğun istek
```

### 2. **Şeffaflık Prensibi**
```
✅ User-Agent'ınızda kim olduğunuzu belirtin
✅ İletişim bilgilerinizi paylaşın
❌ Bot olduğunuzu gizlemeye çalışmayın
```

### 3. **Zarar Vermeme Prensibi**
```
✅ Rate limiting kullanın (istekler arası bekleme)
✅ Hata durumunda denemeleri durdurun
❌ Aynı anda yüzlerce istek göndermeyin
```

## 🤖 robots.txt - Sitenin Kuralları

### robots.txt Nedir?
Web sitelerinin botlara yönelik kurallarını yazdığı dosya:
```
https://example.com/robots.txt
```

### Örnek robots.txt
```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/
Crawl-delay: 5

User-agent: Googlebot
Allow: /

User-agent: BadBot
Disallow: /
```

### Python'da robots.txt Kontrolü
```
İleriki bölümlerde robots.txt dosyasını otomatik olarak 
kontrol eden kod örneklerini öğreneceğiz.

Şimdilik manuel olarak kontrol edin:
1. Tarayıcınızda: https://example.com/robots.txt
2. Scraping yapmak istediğiniz URL'yi kontrol edin
3. "Disallow" listesinde var mı bakın
```

## ⚡ Rate Limiting - Hız Sınırlaması

### Neden Gerekli?
```
Analoji: Market alışverişi
- Normal hız: Her ürünü bakıp alma (Normal kullanıcı)
- Çok hızlı: Koşarak alışveriş yapma (Bot gibi)
- Aşırı hız: Marketi istila etme (DDoS saldırısı)
```

### Rate Limiting Nedir?
```
Rate limiting = İstekler arası bekleme süresi

Örnekler:
- Her istek arasında 1-2 saniye beklemek
- Dakikada maksimum 10 istek göndermek
- Server yoğunken daha uzun beklemek

Bu konuyu 02-bs4-requests bölümünde pratik olarak öğreneceğiz.
```

## 📋 Yasal Durumlar

### ✅ Genellikle Yasal Olan Durumlar
- **Halka açık veriler** (haber siteleri, ürün fiyatları)
- **Kendi sitenizi** scraping yapmak
- **API alternatifi olmayan** durumlar
- **Akademik araştırma** amaçlı kullanım
- **Fiyat karşılaştırma** siteleri

### ⚠️ Dikkatli Olunması Gereken Durumlar  
- **Kişisel veriler** (email, telefon, adres)
- **Telif hakkı korumalı içerik** (resimler, yazılar)
- **Login gerektiren alanlar**
- **Ticari kullanım** 

### ❌ Kesinlikle Yasak Olan Durumlar
- **KVKV ihlali** (kişisel verileri izinsiz kullanma)
- **Sitenin ToS'unu ihlal** (Terms of Service)
- **DDoS benzeri saldırılar**
- **Telif hakkı ihlali**

## 🔒 Kişisel Veri Koruması (KVKV/GDPR)

### KVKV Uyumlu Scraping İlkeleri
```
1. Veri Minimizasyonu
   - Sadece ihtiyacınız olan veriyi toplayın
   - Gereksiz kişisel bilgi almayın

2. Anonimleştirme  
   - Kişisel verileri kimlik belirleyici olmayacak şekilde işleyin
   - Hash fonksiyonları kullanın

3. Saklama Süresi
   - Veriyi süresiz saklamayın
   - Kullanım amacı bitince silin

Teknik detayları ilerki bölümlerde öğreneceğiz.
```

## 🛡️ Etik Scraping Checklist

Scraping yapmadan önce şu soruları kendinize sorun:

### ✅ Teknik Kontroller
- [ ] robots.txt dosyasını kontrol ettim
- [ ] Rate limiting kullanıyorum  
- [ ] User-Agent belirttim
- [ ] Hata durumlarını yönetiyorum
- [ ] Sunucuya zarar vermeyecek şekilde çalışıyor

### ✅ Yasal Kontroller
- [ ] Halka açık verilerle çalışıyorum
- [ ] Kişisel veri toplamıyorum
- [ ] Telif hakkı ihlali yapmıyorum
- [ ] Terms of Service'i okudum
- [ ] Ticari kullanım izinlerim var

### ✅ Etik Kontroller
- [ ] Site sahibi yerinde olsam bu scraping'e razı olur muydum?
- [ ] Veriyi sorumlu şekilde kullanacağım
- [ ] Kaynak web sitesine atıf yapacağım
- [ ] Gerekirse site sahibiyle iletişime geçebilirim

## 💡 İyi Pratikler

### 1. User-Agent Belirtme
```
User-Agent: Web tarayıcınızın kimlik bilgisi
Örnekler: Chrome, Firefox, Safari, veya özel bot adı

İyi örnek: "Educational Bot; contact: email@example.com"
Kötü örnek: Gerçek tarayıcı gibi görünmeye çalışmak
```

### 2. Cache Kullanımı  
```
Cache = Daha önce indirilen sayfaları tekrar kullanma

Avantajları:
- Aynı sayfayı tekrar indirmez
- Server'a daha az yük
- Daha hızlı çalışma

Teknik detayları ileriki bölümlerde.
```

### 3. Hata Yönetimi
```
Nelere dikkat edin:
- Sayfa bulunamadı (404)
- Server hatası (500) 
- Rate limit aşımı (429)
- Bağlantı problemleri

Her durumda nasıl davranacağınızı planlayın.
```

## 🎯 Sonuç

Web scraping yaparken:
1. **Teknik yetkinlik** kadar **etik bilinci** de geliştirin
2. **"Zararsız kullanım"** prensibini benimseyin  
3. **Yasal sınırları** öğrenin ve uygulayın
4. **İyi komşuluk** ilişkileri kurun

**Unutmayın:** Etik scraping, sürdürülebilir scraping demektir. Bugün kurallara uyarsanız, yarın da scraping yapabilirsiniz.

---

**Sonraki adım:** `02-bs4-requests/basic_scrape.py` - İlk örneğimiz!

