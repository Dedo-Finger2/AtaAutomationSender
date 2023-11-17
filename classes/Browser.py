from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Browser:
    driver = None

    def __init__(self, browser: str):
        match browser.upper():
            case "CHOR0ME":
                self.driver = webdriver.Chrome()
            case "EDGE":
                self.driver = webdriver.Edge()
            case "FIREFOX":
                self.driver = webdriver.Firefox()
            case other:
                self.driver = webdriver.Edge()

    def open_page(self, url: str):
        self.driver.get(url)

    def close_driver(self):
        self.driver.close()

    def access_field_by_xpath(self, xpath_value: str, text_value: str):
        sleep(0.5)
        field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_value)))
        field.clear()
        field.send_keys(text_value)
        return field

    def access_field_by_id(self, id_value: str, text_value: str):
        sleep(0.5)
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id_value)))
        field.clear()
        field.send_keys(text_value)

    def click_element(self, by: str | By, attribute_value: str):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, attribute_value)))
        element.click()


    def get_element(self, by: str | By, attribute_value: str):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, attribute_value)))
        return element

