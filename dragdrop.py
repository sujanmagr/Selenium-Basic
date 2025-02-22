#script to drag and drop a file 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
#maximize window
driver.maximize_window()
time.sleep(3)
# drag=WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH, "//div[@id='image']//img"))
# drop=WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH, "//div[@id='box']"))
drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='image']//img")))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='box']")))
ActionChains(driver).drag_and_drop(drag, drop).perform()
time.sleep(3)
driver.quit()

