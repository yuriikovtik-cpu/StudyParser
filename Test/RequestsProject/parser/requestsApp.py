from .models import Tool
import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',  # Do Not Track
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'Trailers',  # Transfer Encoding
}

url = f'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'


def getTools():

    product = {}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')


    try:
        product['title'] = soup.h1.text.strip()
    except AttributeError:
        product['title'] = None
    with open("product.html", "wb") as f:
        f.write(r.text.encode('utf-8'))

    try:
        color = soup.find('div', class_='slice')
        product['color'] = color['style'].split(':')[-1].replace(';', '').strip()
    except (AttributeError, TypeError):
        product['color'] = None

    try:
        product['memory'] = soup.find('div', attrs={'class': 'series-characteristic current on-mob'}).text.strip()
    except AttributeError:
        product['memory'] = None

    try:
        product['price'] = soup.find('div', attrs={'class': 'price-wrapper'}).text.strip()
    except AttributeError:
        product['price'] = None

    try:
        for li in soup.find_all('li', attrs={'role': 'presentation'}):
            product['img_url'].append('https:' + li.find('img', attrs={'class': 'dots-image'}).get('src'))
    except AttributeError:
        product['img_url'] = None
    try:
        product['productCode'] = soup.find('span', attrs={'class': 'br-pr-code-val'}).text.strip()
    except AttributeError:
        product['productCode'] = None

    try:
        for comment_block in soup.find_all('div', class_='br-comment-text loaded'):
            p = comment_block.find('p')
            if p:
                product['comments'].append(p.text.strip())
    except AttributeError:
        product['comment'] = None

    try:
        product['screen_diagonal'] = soup.find('span', string='Діагональ екрану').find_next_sibling('span').text.strip()
    except AttributeError:
        product['screen_diagonal'] = None

    try:
        product['screen_resolution'] = soup.find('span', string='Роздільна здатність екрану').find_next_sibling('span').text.strip()
    except AttributeError:
        product['screen_resolution'] = None

    try:
        specifications = soup.find('div', attrs={'id':'br-pr-7','class': 'br-pr-tblock br-pr-chr-wrap'})
        product['specifications'] = specifications.text.strip().replace('\n\n', ' ')
        specifications.decompose()
    except AttributeError:
        product['specifications'] = None

    for key, value in product.items():
        print('=' * 50)
        print(f'{key}: {value}')

    Tool.objects.create(**product)

    df = pd.DataFrame([product])
    df.to_csv(r'\results\productsRequests.csv', index=False)

    return product
