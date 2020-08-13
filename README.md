# Ians-Player-Predictions-Spider
A Python program that uses Scrapy to scrape baseball statistics from [https://baseballsavant.mlb.com](https://baseballsavant.mlb.com) to use to calculate players that should start improving or getting worse.

## Directions:
- Install Docker at [https://www.docker.com/get-started](https://www.docker.com/get-started)
- Run `source update.sh` in terminal to set up Splash and install dependencies
- Navigate into Scrapy-Ians-Player-Predictions directory and run `scrapy crawl PlayerSpider -o data.json` to run spider
- Check Scrapy-Ians-Player-Predictions directory for data.json, which will hold the output of PlayerSpider.

## Other Information:
- An up to date output of this spider is kept in [this AWS S3 bucket](https://s3.amazonaws.com/scrapy.crawled.data/MLBPlayerPredictions/data.json).
- The data scraped using this spider is used for the [Ians-Player-Predictions](https://github.com/ianwood103/Ians-Daily-Predictions) repository.
