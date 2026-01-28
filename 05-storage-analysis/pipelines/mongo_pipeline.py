import pymongo
from itemadapter import ItemAdapter

class MongoPipeline:
    """
    Scrapy item'larını MongoDB veritabanına kaydeder.
    """
    
    collection_name = 'quotes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # Ayarları settings.py'dan al
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://localhost:27017'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'scraping_db')
        )

    def open_spider(self, spider):
        # Spider başladığında veritabanına bağlan
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        print(f"✅ MongoDB Bağlantısı Başarılı: {self.mongo_db}")

    def close_spider(self, spider):
        # Spider bittiğinde bağlantıyı kapat
        self.client.close()

    def process_item(self, item, spider):
        # Veriyi dict'e çevir ve kaydet
        data = ItemAdapter(item).asdict()
        
        # Duplicate kontrolü (aynı text varsa kaydetme)
        if self.db[self.collection_name].count_documents({'text': data['text']}) == 0:
            self.db[self.collection_name].insert_one(data)
            # print(f"💾 MongoDB'ye kaydedildi: {data['author']}")
        else:
            pass
            # print(f"⚠️ Duplicate veri: {data['author']}")
            
        return item