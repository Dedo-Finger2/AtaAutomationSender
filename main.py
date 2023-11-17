from time import sleep
from classes.Browser import Browser
from classes.Trello import Trello
from classes.XpathBuilder import XpathBuilder
import secret
from classes.FileManagment import FileManagment

# ----------------------------------------------------------------------------------------------------------------------
# browser = Browser("edge")
# browser.open_page("https://www.bing.com/search?q=input+html+test&qs=n&form=QBRE")
# browser.access_field_by_id("sb_form_q", "Olá")
# sleep(60)
# browser.close_driver()

# ----------------------------------------------------------------------------------------------------------------------
# LOGIN TRELLO
trello = Trello('edge', 'https://trello.com/b/nmUvjDF5/tcc-geral')
trello.login(secret.email, secret.password)
trello.add_card_to_list("653d97eb10388f15c193b915", "ATA - 17/11/2023").enter_card("ATA - 17/11/2023")
trello.add_attachments()
sleep(300)
trello.close_driver()

# ----------------------------------------------------------------------------------------------------------------------
# XPATH BUIDLER
# print(XpathBuilder.simple_xpath("Input", "id", "login-submit"))

# layers = [
#     "div",
#     "div",
#     "li",
#     "h2",
# ]
#
# print(XpathBuilder.nested_xpath(layers, "text()='ATAs'"))

# ----------------------------------------------------------------------------------------------------------------------
# for file in FileManagment.get_files("attachments"):
#     print(file)

