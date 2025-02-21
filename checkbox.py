#script to click buttons 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/checkbox"
driver.get(url)
#maximize window
driver.maximize_window()
#finding checkboxes with their id or XPATH
checkbox1=driver.find_element(By.ID, "checkbox-1")
checkbox2=driver.find_element(By.ID, "checkbox-2")
checkbox3=driver.find_element(By.ID, "checkbox-3")

#clicking checkboxe
checkbox1.click()
time.sleep(1)
checkbox2.click()
time.sleep(1)
checkbox3.click()
#close window after 3 sec
time.sleep(3)
driver.quit()