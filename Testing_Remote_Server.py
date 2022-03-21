from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='192.0.0.1:9222',
    options=chrome_options
)
driver.get("https://youtube.com")