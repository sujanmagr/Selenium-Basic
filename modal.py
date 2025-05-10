#script to open a model and close it
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/modal"
driver.get(url)
#maximize window
driver.maximize_window()
#find the button of open
button1=driver.find_element(By.ID, "modal-button")
button1.click()
time.sleep(5)

#close the modal
close=driver.find_element(By.ID, "close-button")
close.click()

time.sleep(2)
driver.quit()
