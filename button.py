#script to click buttons 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/buttons#"
driver.get(url)
#maximize window
driver.maximize_window()
#finding button by their XPATH or id or any selector
primary=driver.find_element(*(By.XPATH,"//button[normalize-space()='Primary']"))
success=driver.find_element(*(By.XPATH,"//button[normalize-space()='Success']"))
info=driver.find_element(*(By.XPATH,"//button[normalize-space()='Info']"))
link=driver.find_element(*(By.XPATH,"//button[normalize-space()='Link']"))
dropdown=driver.find_element(*(By.XPATH,"//button[@id='btnGroupDrop1']"))
dropdown_option1=driver.find_element(*(By.XPATH,"//a[normalize-space()='Dropdown link 1']"))
#clicking the buttons
try:
    primary.click()
    print("primary clicked")
except:
    print("primary not clicked")
time.sleep(1)
success.click()
print("success clicked")
time.sleep(1)
info.click()
print("info clicked")
time.sleep(1)
link.click()
print("link clicked")
time.sleep(1)
dropdown.click()
print("drown clicked")
time.sleep(1)
dropdown_option1.click()
print("chose option 1")
time.sleep(1)
#quit the window after a while
time.sleep(3)
driver.quit()