import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/another-worlds-versatile-crafting-master/',
	    'https://www.worldnovel.online/novel/i-have-countless-legendary-swords/',
	    'https://www.worldnovel.online/novel/god-of-soul-system/',
	    'https://www.worldnovel.online/novel/i-might-be-a-fake-cultivator/',
	    'https://www.worldnovel.online/novel/scholars-advanced-technological-system/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')