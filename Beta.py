from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import siderunner
import os


class SF_Copilot():
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument(r"--user-data-dir=C:\Users\tre.grinner\AppData\Local\Google\Chrome\User\Data")
        self.options.add_argument(r'--profile-directory=Profile 6')
        self.options.add_argument(r'--remote-debugging-port=9222')
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
        self.driver = None
        self.session_id = None  # Session ID of this driver instance
        self.executor_url = None  # executor_url

    def print_driver_details(self):
        print('Sales Force Co-Pilot Driver Initialized!:\n', self.driver.capabilities)
        self.command_executor_url = self.driver.command_executor._url
        print(r'Command Executor URL:', self.command_executor_url)
        print(r'Session ID:', self.driver.session_id)

    def start_driver(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        print("SF Co-Pilot Driver Started!:", self.driver.capabilities)


class Close_Copilot():
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument(r"--user-data-dir=C:\Users\tre.grinner\AppData\Local\Google\Chrome\User\Data")
        self.options.add_argument(r'--profile-directory=Profile 5')
        self.options.add_argument(r'--remote-debugging-port=9223')
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = None  # Driver object
        self.session_id = None  # Session ID of this driver instance
        self.command_executor_url = None  # Executor_url
        self.desired_remote_capabilities = {}

    def print_driver_details(self):
        print('CLose Co-Pilot Driver Initialized!:\n', self.driver.capabilities)
        self.command_executor_url = self.driver.command_executor._url
        print(r'Command Executor URL:', self.command_executor_url)
        print(r'Session ID:', self.driver.session_id)

    def test_command(self):
        self.driver.get("https://close.com")

    def start_driver(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.print_driver_details()

    def command(self):
        webdriver.Remote(command_executor=type(self.command_executor_url, ))


while True:
    a = Close_Copilot()
    a.start_driver()
