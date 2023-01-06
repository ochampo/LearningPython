from selenium import webdriver

driver = webdriver.Chrome(executable_path = '.\chromedriver.exe')

driver.get('https://testpages.herokuapp.com/styled/validation/input-validation.html')

messageField = driver.find_element_by_xpath('//*[@id="firstname"]')
messageField.send_keys('Dan')