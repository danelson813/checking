from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


def get_url(i: int) -> str:
    """
    use the counter i to get the correct url
    output is a url
    """
    return f"https://books.toscrape.com/catalogue/page-{i}.html"

def save_soup(soup: BeautifulSoup, filename: str) -> None:
    '''
        once the soup is created for the url 
        save it to disk for future use
    '''
    with open(f'{filename}', 'w') as f:
        f.write(str(soup))

def get_soup_req(url_:str) -> BeautifulSoup:
    '''
    start with a url and form a beautifulsoup object
    fake-useragent is used to vary the useragent to keep from
    being rejected.
    '''
    ua = UserAgent()
    useragent = ua.random
    session = requests.Session()
    session.headers.update({'User-Agent': f'{useragent}'})
    resp = session.get(url_)
    
    # print(resp.status_code)

    soup = BeautifulSoup(resp.text, 'html.parser')

    # save_soup(soup,filename)
    return soup
