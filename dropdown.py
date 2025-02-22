from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/dropdown"
driver.get(url)
#maximize window
driver.maximize_window()
dropdown1=driver.find_element(By.ID, "dropdownMenuButton")
dropdown1.click()
time.sleep(2)
option_click=driver.find_element(By.XPATH, "/html/body/div/div/div/a[5]")
option_click.click()
time.sleep(2)
driver.quit()
