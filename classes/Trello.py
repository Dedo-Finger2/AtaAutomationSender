from classes.Browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from classes.FileManagment import FileManagment
from time import sleep
import pyautogui
import shutil


class Trello(Browser):
    def __init__(self, browser: str, url: str):
        super().__init__(browser)
        self.open_page(url)

    def login(self, email: str, password: str):
        # Clica no link para acessar o formulário de login
        self.click_element(By.XPATH, "//button[@data-testid='request-access-login-button']")
        # Acessa o input de email e cola o email nele
        self.access_field_by_xpath("//input[@placeholder='Enter email']", email)
        # Clica no botão de continuar
        self.click_element(By.XPATH, "//input[@id='login']")
        # Acessa o input de senha e cola a senha nele
        self.access_field_by_xpath("//input[@placeholder='Enter password']", password)
        # Efetua o login
        self.click_element(By.XPATH, "//button[@id='login-submit']")

    def add_card_to_list(self, data_list_id: str, card_title: str):
        list_column = f"//li[@data-list-id='{data_list_id}']"
        add_card_button = list_column + "//button[@data-testid='list-add-card-button']"
        self.click_element(By.XPATH, add_card_button)
        element = self.access_field_by_xpath("//textarea[@placeholder='Enter a title for this card…']",
                                             card_title)
        element.send_keys(Keys.RETURN)
        return self

    def enter_card(self, card_title: str):
        sleep(1)
        self.click_element(By.XPATH, f'//div[@data-testid="trello-card" and .//a[text()="{card_title}"]]')

    def add_attachments(self):
        for file in FileManagment.get_files("attachments"):
            self.click_element(By.XPATH, "//div[@class="
                                         "'js-new-card-attachment-picker-react-root-for-sidebar']/div/button")
            sleep(1)
            # Clicar upload
            pyautogui.click(850,318, duration=1)
            # Clicar url windows
            pyautogui.click(638,63, duration=1)
            # escrever
            pyautogui.write("C:\\Users\\anton\\Documents\\PycharmProjects\\AtaAutomationSender\\attachments")
            # enter
            pyautogui.press('enter')
            # arquivo
            pyautogui.click(311,171, duration=1)
            # open
            pyautogui.click(808,518, duration=1)
            sleep(3)
            shutil.move(f"attachments/{file}",
                        f"attachmentsSent/{file}")

