from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument("user-data-dir=C:\Program Files\Google\Chrome\Application\99.0.4844.51")
#options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://blancco.lightning.force.com/lightning/r/Account/0010O00001jRyF5QAK/related/Contacts/view")
info_card = driver.find_element(By.ID, "div.slds-tabs_card")
print(info_card)
driver.quit()
