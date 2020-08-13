import scrapy
from scrapy_splash import SplashRequest


class PlayerspiderSpider(scrapy.Spider):
    name = 'PlayerSpider'
    allowed_domains = ['mlb.com']
    def start_requests(self):
        urls = [
            'https://baseballsavant.mlb.com/leaderboard/expected_statistics?type=batter&year=2020&position=&team=&min=q&sort=13&sortDir=asc',
            'https://baseballsavant.mlb.com/leaderboard/expected_statistics?type=batter&year=2020&position=&team=&min=q&sort=13&sortDir=desc'
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={"wait": 3})

    def parse(self, response):
        tableRows = response.css('div #expected_stats table tr td')
        players = tableRows.css('span a::text').getall()
        headshots = tableRows.css('img.player-mug::attr(src)').getall()
        logos = tableRows.css('img.table-team-logo::attr(src)').getall()
        for num in range(0, 5):
            yield {
                "player": players[num],
                "headshot": headshots[num],
                "logo": logos[num]
            }
