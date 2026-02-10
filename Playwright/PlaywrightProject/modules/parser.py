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
            specifications = {}
            items = page.locator("div.br-pr-chr-item").all()
            for item in items:
                h3 = item.locator("h3").first
                if h3.count() == 0:
                    continue

                category_name = h3.inner_text().strip()
                specifications[category_name] = {}
                rows = item.locator("xpath=.//h3/following-sibling::div[1]/div").all()
                for row in rows:
                    spans = row.locator("span").all()

                    if len(spans) >= 2:
                        key = spans[0].inner_text().strip()
                        value = spans[1].inner_text().strip().replace('\xa0', ' ')
                        specifications[category_name][key] = value

            productList['specifications'] = specifications
            flat_product = productList.copy()
            specs_to_flatten = flat_product.pop('specifications', {})

            if specs_to_flatten:
                for category, params in specs_to_flatten.items():
                    for key, value in params.items():
                        flat_product[f"{category}: {key}"] = value
        except AttributeError:
            productList['specifications'] = None

        for key, value in productList.items():
            print('=' * 50)
            print(f'{key}: {value}')
        Tool.objects.create(**productList)

        df = pd.DataFrame([productList])
        output_dir = r'D:\Python\PycharmProjects\Playwright\PlaywrightProject\modules\results'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'product.csv')

        df.to_csv(output_file, index=False)
        return productList

