from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome(executable_path = '.\chromedriver.exe')

# driver.get('https://testpages.herokuapp.com/styled/validation/input-validation.html')

# messageField = driver.find_element_by_xpath('//*[@id="firstname"]')
# messageField.send_keys('Dan')


##### drag example 

driver2 = webdriver.Chrome(executable_path = '.\chromedriver.exe')
driver2.get('http://www.seleniumframework.com/Practiceform/')
source = driver2.find_element_by_xpath('//*[@id="draga"]')
dest = driver2.find_element_by_xpath('//*[@id="dragb"]')


actions = ActionChains(driver2)

actions.drag_and_drop(source,dest).perform()
