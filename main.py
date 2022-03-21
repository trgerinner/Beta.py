import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options, ChromiumOptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

def start_server(name=None):
    session_name = name
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.page_load_strategy = 'none'
    browser = webdriver.Chrome(service=service, options=options)


def driver_update():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)


def list_capibilites(self):
    print(self.browser.capabilities)


def list_windows(self):
    print("current windows:", self.browser.window_handles)


def teardown(self):
    self.browser.quit()


start_server("test")

start_server("testserver")
