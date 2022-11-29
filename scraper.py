import requests as requests
import bs4 as bs4
import constants as _const


#url yaratmak için
def _create_url(tag: str) -> str:
    return f"https://www.goodreads.com/quotes/tag/{tag}"


#sayfayı almak için
def _get_page(url: str) -> bs4.BeautifulSoup:
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")

    return soup

#yazar adi ve yaziyi çikarmak için
def _extract_quote_and_author(quote):
    quote_text = quote.contents[0].strip()
    author = quote.find(class_ ="authorOrTitle").text.strip()
    return quote_text, author

#ana fonksiyon
def scrape_quotes():
    collection = list()
    for tag in _const.TAGS:
        url = _create_url(tag)
        soup = _get_page(url)
        raw_quotes = soup.find_all(class_= "quoteText")
        for quote in raw_quotes:
            quote_text, author = _extract_quote_and_author(quote)
            data = { "quote": quote_text, "author": author, "genre": tag }
            collection.append(data)
    
    return collection


    