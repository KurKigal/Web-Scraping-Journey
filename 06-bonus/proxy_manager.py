import requests
from fake_useragent import UserAgent
import random
import time

class RequestManager:
    """
    Anti-ban önlemleri içeren gelişmiş istek yöneticisi.
    Otomatik User-Agent ve Proxy rotasyonu sağlar.
    """
    
    def __init__(self, proxy_list=None):
        # Rastgele User-Agent üretici
        self.ua = UserAgent()
        
        # Proxy listesi (Gerçek hayatta buraya satın aldığınız proxy'ler gelir)
        # Format: "http://user:pass@ip:port" veya "http://ip:port"
        self.proxy_list = proxy_list if proxy_list else []
        
    def get_random_headers(self):
        """Her istek için rastgele bir tarayıcı kimliği üretir"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

    def get_random_proxy(self):
        """Listeden rastgele bir proxy seçer"""
        if not self.proxy_list:
            return None
            
        proxy = random.choice(self.proxy_list)
        return {
            "http": proxy,
            "https": proxy
        }

    def make_request(self, url):
        """Rotasyonlu istek atar"""
        headers = self.get_random_headers()
        proxies = self.get_random_proxy()
        
        print(f"🔄 İstek atılıyor: {url}")
        print(f"🎭 Kimlik: {headers['User-Agent'][:30]}...")
        if proxies:
            print(f"🌍 Proxy: {proxies['http']}")
        
        try:
            # Proxy varsa proxyli, yoksa proxysiz istek
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            
            if response.status_code == 200:
                print("✅ Başarılı!")
                return response
            else:
                print(f"❌ Hata Kodu: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"💥 Bağlantı Hatası: {str(e)}")
            return None

# --- TEST KISMI ---
if __name__ == "__main__":
    # Örnek Kullanım
    
    # Not: Buradaki proxy'ler örnektir, çalışmayabilir.
    # Ücretsiz proxy listeleri genelde çok kısa ömürlüdür.
    sample_proxies = [
        # "http://1.2.3.4:8080",
        # "http://5.6.7.8:3128"
    ]
    
    manager = RequestManager(proxy_list=sample_proxies)
    
    # httpbin.org sitesi IP adresimizi ve User-Agent'ımızı bize geri söyler
    test_url = "https://httpbin.org/user-agent"
    
    print("🧪 TEST 1:")
    manager.make_request(test_url)
    
    print("\n🧪 TEST 2 (Farklı User-Agent görmeliyiz):")
    manager.make_request(test_url)