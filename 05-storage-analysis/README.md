
# 📊 Veri Depolama (NoSQL) ve Analiz

Scraping sadece veri çekmek değildir; o veriyi yönetmek ve ondan değer üretmektir. Bu bölümde scraping dünyasının "End Game"i olan iki konuyu işleyeceğiz:
1. **MongoDB:** Büyük ve düzensiz verileri depolamak için endüstri standardı.
2. **Data Analysis:** Çekilen veriden grafikler ve içgörüler (insight) çıkarmak.

## 🛠️ Kurulum

### 1. Python Kütüphaneleri
Analiz ve veritabanı bağlantısı için gerekli paketleri kurun:

```
pip install -r requirements.txt
````

### 2. MongoDB Kurulumu (Docker ile)

MongoDB'yi bilgisayarınıza kurmanın en temiz yolu Docker kullanmaktır.

Bash

```
# MongoDB container'ını başlat
docker run -d -p 27017:27017 --name mongo-scraping mongo:latest
```

_Eğer Docker kullanmıyorsanız, [MongoDB Community Server](https://www.mongodb.com/try/download/community) indirip kurabilirsiniz._

## 📂 İçerik

### `pipelines/mongo_pipeline.py`

Bu dosya, Scrapy projenize (03-scrapy) entegre edebileceğiniz bir pipeline'dır. Verileri JSON yerine doğrudan veritabanına atmanızı sağlar.

### `analysis/data_analysis.ipynb`

Çekilen verilerin görselleştirilmesi:

- En çok konuşan yazarlar (Bar Chart)
    
- Popüler etiketler (WordCloud)
    
- Alıntı uzunluk analizleri (Histogram)
    

### `analysis/sentiment_analysis.ipynb`

Metin madenciliği giriş:

- Alıntılar pozitif mi negatif mi?
- En "mutlu" yazar kim?