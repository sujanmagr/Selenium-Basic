#scripts to switch window or tabs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
driver.maximize_window()
time.sleep(2)
alert=driver.find_element(By.ID, "alert-button")
newTab=driver.find_element(By.ID, "new-tab-button")

#click the buttons
alert.click()
alert1=Alert(driver)
alert1.accept()#accept the alert
print("alert accepted")
time.sleep(2)
#button to switch window
newTab.click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
print("mouse is on new tab")
#find element on new tab
autocomplete=driver.find_element(*(By.XPATH,"//a[@class='btn btn-lg'][normalize-space()='Autocomplete']"))
autocomplete.click()
time.sleep(1)
driver.quit()