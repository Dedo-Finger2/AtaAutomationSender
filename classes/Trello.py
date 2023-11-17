from classes.Browser import Browser
from selenium.webdriver.common.by import By


class Trello(Browser):
    def __init__(self, browser: str, url: str):
        super().__init__(browser)
        self.open_page(url)

    def login(self, email: str, password: str):
        self.click_element(By.XPATH, "//button[@data-testid='request-access-login-button']")
        self.access_field_by_xpath("//input[@placeholder='Enter email']", email)
        self.click_element(By.XPATH, "//input[@id='login']")
        self.access_field_by_xpath("//input[@placeholder='Enter password']", password)
        self.click_element(By.XPATH, "//button[@id='login-submit']")
