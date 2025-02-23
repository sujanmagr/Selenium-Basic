#script for key press
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/keypress"
driver.get(url)
#maximize window
driver.maximize_window()
#find the input fields
full_name=driver.find_element(By.ID, "name")
Button=driver.find_element(By.ID, "button")
#fillup the input fields and click the buttton
full_name.send_keys("Sachin Budhathoki")
time.sleep(2)
try:
    Button.click()
    print("button is clicked")

except:
    print("button is not clicked")

time.sleep(3)
driver.quit()