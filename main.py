from time import sleep
from classes.Browser import Browser
from classes.Trello import Trello
from classes.XpathBuilder import XpathBuilder
import secret

# browser = Browser("edge")
# browser.open_page("https://www.bing.com/search?q=input+html+test&qs=n&form=QBRE")
# browser.access_field_by_id("sb_form_q", "Olá")
# sleep(60)
# browser.close_driver()

trello = Trello('edge', 'https://trello.com/b/nmUvjDF5/tcc-geral')
trello.login(secret.email, secret.password)
sleep(120)
trello.close_driver()

# print(XpathBuilder.simple_xpath("Input", "id", "login-submit"))
