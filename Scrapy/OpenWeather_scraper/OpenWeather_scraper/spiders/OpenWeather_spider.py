import scrapy

class OpenWeatherSpider(scrapy.Spider):
    name = "OpenWeather_spider"
    start_urls = ["https://openweathermap.org/"]

    def parse(self, response):
        headlines = response.css("h2::text").getall()
        for i, headline in enumerate(headlines[:10], start=1):
            yield {"No": i, "Headline": headline.strip()}
