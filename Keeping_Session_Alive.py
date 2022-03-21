from webdriver_manager.chrome import ChromeDriverManager
# Driver Manager to keep the driver matched with the most recent version of chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

class Session():
    def __init__(self):
        self.

def connect():
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        global browser
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except Exception as e:
        print(e)


connection = connect()
