#script to scroll the page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/scroll"
driver.get(url)
#maximize window
driver.maximize_window()
time.sleep(2)
#calculate height
page_height=driver.execute_script("return document.body.scrollHeight")
scroll_speed=500
scroll_iteration=int(page_height/scroll_speed)
#perform scroll
for _ in range (scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(3)

#find input fields at the end of page
fullName=driver.find_element(By.ID, "name")
date=driver.find_element(By.ID, "date")

#send input values
fullName.send_keys("Sachin Budhathoki")
date.send_keys("02/12/2025")

time.sleep(3)
driver.quit()