from base64 import decode, encode
from codecs import ascii_decode
import json as json
import scraper as scraper

if __name__ == "__main__":
    quotes = scraper.scrape_quotes()
    with open(".\src\quotes.json",mode="w") as quotes_file:
        json.dump(quotes,quotes_file)