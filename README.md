# 🕷️ Web Scraping Journey

> **Not:** Bu repo, Python temellerine hâkim olduğunuzu varsayar.  
> Eğer Python bilmiyorsanız, hazırladığım [Data Science reposunu](https://github.com/KurKigal/Data-Science-Journey) inceleyebilirsiniz. 


## 📋 İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Kurulum](#kurulum)
- [Bölümler](#bölümler)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)

## 🎯 Proje Hakkında

Bu repo, web scraping öğrenmek isteyenler için kapsamlı bir eğitim kaynağıdır. Temel kavramlardan başlayıp profesyonel scraping tekniklerine kadar her şeyi öğreneceksiniz.

### Ne Öğreneceksiniz?
- ✅ Web scraping'in temel prensipleri
- ✅ Requests + BeautifulSoup ile basit scraping
- ✅ Scrapy framework kullanımı
- ✅ JavaScript render edilen siteleri scraping
- ✅ Veri depolama ve analiz teknikleri
- ✅ Etik ve yasal konular

## 🛠️ Kurulum

### Gereksinimler
- Python 3.8+
- pip (Python paket yöneticisi)

### Adım 1: Repo'yu İndirin
```bash
git clone https://github.com/KurKigal/Web-Scraping-Journey.git
cd Web-Scraping-Journey
```

### Adım 2: Virtual Environment Oluşturun
```bash
python3 -m venv scraping_env
source scraping_env/bin/activate  # Linux/Mac
# scraping_env\Scripts\activate   # Windows
```

### Adım 3: Gerekli Paketleri Kurun
```bash
pip install -r requirements.txt
```

## 📚 Bölümler

### [01 - Giriş](01-intro/)
- Web scraping nedir?
- Etik ve yasal konular

### [02 - BeautifulSoup + Requests](02-bs4-requests/)
- Temel scraping teknikleri
- Pagination ve login işlemleri

### [03 - Scrapy Framework](03-scrapy/)
- Profesyonel web scraping
- Büyük ölçekli projeler

### [04 - JavaScript Rendering](04-splash-js/)
- Modern web sitelerini scraping
- Splash kullanımı

### [05 - Depolama ve Analiz](05-storage-analysis/)
- Veriyi kaydetme yöntemleri
- Basit analiz ve görselleştirme

### [06 - Bonus](06-bonus/)
- Proxy kullanımı
- Asenkron scraping

## 🚀 Kullanım

Her bölümü sırasıyla takip edin. Her klasörde örnek kodlar ve açıklamalar bulunur.

```bash
cd 01-intro
# Önce dökümanları okuyun
# Sonra kod örneklerini çalıştırın
```

## 🤝 Katkıda Bulunma

Bu projeyi geliştirmek için:
1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push yapın (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında yayınlanmıştır.

## ⚠️ Uyarı

Web scraping yaparken:
- Sitelerin robots.txt dosyasına uyun
- Rate limiting kullanın
- Sunuculara zarar vermeyin
- Yasal sınırları aşmayın
