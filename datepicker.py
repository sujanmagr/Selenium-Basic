#script to pick a date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/datepicker"
driver.get(url)
#maximize window
driver.maximize_window()
#find date field 
date_field=driver.find_element(By.ID, "datepicker")
#send data using send keys in format m/dd/yyyy
date_field.send_keys("03/12/2023")
# close window after 3 sec
time.sleep(3)
driver.quit()
