import scrapy


class PdfspiderSpider(scrapy.Spider):
    name = "pdfspider"
    allowed_domains = ["www.pdfdrive.com"]
    start_urls = ["https://www.pdfdrive.com/"]

    def parse(self, response):
        pass


