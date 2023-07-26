import scrapy


class PdfspiderSpider(scrapy.Spider):
    name = "pdfspider"
    allowed_domains = ["www.pdfdrive.com"]
    start_urls = ["https://www.pdfdrive.com/"]

    def parse(self, response):
        books = response.css(".file-info")

        for book in books:
            yield {
                "Title" : book.css('a h2::text').get(),
                "Pages" : book.css('.file-info .fi-pagecount::text').get(),
                "Year" : book.css('.file-info .fi-year::text').get()



            }



