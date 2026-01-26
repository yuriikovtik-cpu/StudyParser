import os

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class FindInfo:

    def find(self,driver):
        productList = {}
        try:
            productList['title'] = driver.find_element(By.XPATH,"//h1[@class='main-title']").get_attribute("textContent").strip()
        except NoSuchElementException:
            productList['title'] = None

        try:
            productList['color'] = driver.find_element(By.XPATH,"//a[contains(@title, 'Колір')]").get_attribute("textContent")
        except (NoSuchElementException):
            productList['color'] = None

        try:
            productList['memory'] = driver.find_element(By.XPATH,"//a[contains(@title, 'Вбудована пам')]").get_attribute("textContent")
        except NoSuchElementException:
            productList['memory'] = None

        try:
            productList['price'] = driver.find_element(By.XPATH,"//div[@class = 'price-wrapper']//span[not(@class)]").text.strip()
        except NoSuchElementException:
            productList['price'] = None
        try:
            productList['redPrice'] = driver.find_element(By.XPATH,"//div[@class = 'price-wrapper']//span[@class = 'red-price']").text.strip()
        except NoSuchElementException:
            productList['redPrice'] = None
        try:
            productList['productCode'] = driver.find_element(By.XPATH,"//div[@class = 'title']//span[@class = 'br-pr-code-val']").text.strip()
        except NoSuchElementException:
            productList['productCode'] = None

        try:
            productList['screen_diagonal'] = driver.find_element(By.XPATH,"//a[contains(@title, 'Діагональ екрану')]").get_attribute("textContent")
        except NoSuchElementException:
            productList['screen_diagonal'] = None

        try:
            productList['screen_resolution'] = driver.find_element(By.XPATH,"//a[contains(@title, 'Роздільна здатність екрану')]").get_attribute("textContent")
        except NoSuchElementException:
            productList['screen_resolution'] = None

        try:
            specifications = driver.find_element(By.XPATH,"//div[@id = 'br-pr-7']")
            productList['specifications'] = specifications.text.strip().replace('\n\n', ' ')
        except NoSuchElementException:
            productList['specifications'] = None

        df = pd.DataFrame([productList])
        output_dir = r'D:\Python\PycharmProjects\Selenium\project\result'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'product.csv')

        df.to_csv(output_file, index=False)
        return productList

