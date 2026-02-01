import os
import pandas as pd
from .models import Tool


class FindInfo:

    def find(self, page):
        productList = {}
        try:
            productList['title'] = page.locator("//h1[@class='main-title']").inner_text().strip()
        except AttributeError:
            productList['title'] = None

        try:
            productList['color'] = page.locator("//a[contains(@title, 'Колір')]").inner_text()
        except AttributeError:
            productList['color'] = None

        try:
            productList['memory'] = page.locator("//a[contains(@title, 'Вбудована пам')]").inner_text()
        except AttributeError:
            productList['memory'] = None

        try:
            productList['price'] = page.locator("//div[@class = 'price-wrapper']//span[not(@class)]").inner_text()
        except AttributeError:
            productList['price'] = None
        try:
            productList['redPrice'] = page.locator("//div[@class = 'price-wrapper']//span[@class = 'red-price']").inner_text()
        except AttributeError:
            productList['redPrice'] = None
        try:
            productList['productCode'] = page.locator("//div[@class = 'title']//span[@class = 'br-pr-code-val']").inner_text()
        except AttributeError:
            productList['productCode'] = None

        try:
            productList['screen_diagonal'] = page.locator("//a[contains(@title, 'Діагональ екрану')]").inner_text()
        except AttributeError:
            productList['screen_diagonal'] = None

        try:
            productList['screen_resolution'] = page.locator("//a[contains(@title, 'Роздільна здатність екрану')]").inner_text()
        except AttributeError:
            productList['screen_resolution'] = None

        try:
            specifications = page.locator("//div[@class = 'br-pr-tblock br-pr-chr-wrap']").inner_text()
            productList['specifications'] = specifications.replace('\n\n', ' ')
        except AttributeError:
            productList['specifications'] = None

        for key, value in productList.items():
            print('=' * 50)
            print(f'{key}: {value}')
        Tool.objects.create(**productList)

        df = pd.DataFrame([productList])
        output_dir = r'D:\Python\PycharmProjects\Playwright\PlaywrightProject\ParseApp\results'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'product.csv')

        df.to_csv(output_file, index=False)
        return productList

