import scrapy
from scrapy_splash import SplashRequest

class JsSpider(scrapy.Spider):
    name = "js_spider"
    
    # JavaScript ile yüklenen örnek bir site (Quotes to Scrape JS versiyonu)
    # Bu sayfaya normal request atarsanız alıntıları göremezsiniz.
    start_urls = ["http://quotes.toscrape.com/js/"]

    def start_requests(self):
        for url in self.start_urls:
            # Standart Request yerine SplashRequest kullanıyoruz
            yield SplashRequest(
                url=url,
                callback=self.parse,
                args={
                    'wait': 2,  # Sayfa yüklendikten sonra JS'in çalışması için 2 saniye bekle
                    # 'lua_source': ..., # İleride buraya script vereceğiz
                }
            )

    def parse(self, response):
        # Artık response.text içinde JS tarafından yüklenmiş HTML var!
        # Standart Scrapy seçicilerini kullanabiliriz.
        
        quote_divs = response.css('div.quote')
        
        if not quote_divs:
            self.logger.warning("⚠️ Hiç alıntı bulunamadı! Splash çalışmıyor olabilir.")
        
        for quote in quote_divs:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Pagination (Sayfalama) - JS render edilen sayfalarda link takibi
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            # Linki mutlak URL'e çevir
            next_url = response.urljoin(next_page)
            
            # Sonraki sayfa da JS gerektirdiği için yine SplashRequest
            yield SplashRequest(
                url=next_url,
                callback=self.parse,
                args={'wait': 2}
            )