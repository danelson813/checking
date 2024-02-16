# main.py
import pandas as pd

from utils.util import get_soup_req, get_url


def main(url_: str) -> list:
    soup = get_soup_req(url_)
    books = soup.select('article')
    for book in books:
        result = {
            'title': book.find('img')['alt'],
            'price': book.select_one('p.price_color').text[2:]
        }
        results.append(result)

    return results


if __name__ == '__main__':
    results = []
    for i in range(1, 51):
        temp = main(get_url(i))

    df = pd.DataFrame(results)
    df.to_csv('data/results.csv', index=False)
