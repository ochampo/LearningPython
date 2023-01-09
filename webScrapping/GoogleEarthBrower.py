from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

url = 'https://www.google.com/earth/'

driver = webdriver.Chrome(executable_path = '.\chromedriver.exe')
driver.get(url)

wait = WebDriverWait(driver, 10)