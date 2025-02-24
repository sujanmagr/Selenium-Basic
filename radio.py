#scripts to click radio buttons
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://formy-project.herokuapp.com/radiobutton"
driver.get(url)
driver.maximize_window()
time.sleep(2)
radio1=driver.find_element(By.ID, "radio-button-1")
radio2=driver.find_element(*(By.XPATH,"//input[@value='option2']"))
radio3=driver.find_element(*(By.XPATH,"//input[@value='option3']"))
#click the buttons
radio1.click()
print("radio button 1 clicked")
time.sleep(1)
radio2.click()
print("radio button 2 clicked")
time.sleep(1)
radio3.click()
print("radio button 3 clicked")
time.sleep(2)
driver.quit()