import json as json
from typing import Dict, List
import random as random

def _get_quotes() -> List:
    with open(".\src\quotes.json") as quotes_file:
        quotes = json.load(quotes_file)

    return quotes

def _get_random_quote() -> Dict:
    quotes = _get_quotes()
    quote = random.choice(quotes)

    return quote


def _form_tweet(quote: Dict[str,str]) -> str:
    author = quote["author"].strip(",")
    tweet = f"{quote['quote']} - {author}"

    return tweet

def _is_valid_charecters(tweet: str) -> bool:
    return len(tweet) <= 270

def get_tweet():
    while True:
        quote = _get_random_quote()
        tweet = _form_tweet(quote)
        if _is_valid_charecters(tweet):
            return tweet


