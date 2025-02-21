#script to fill up a simple form 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/autocomplete"
driver.get(url)
driver.maximize_window()
#had to scroll as the zip code and country is not visible in the first view
driver.execute_script("window.scrollBy(0,200);")
#finding input fields
address=driver.find_element(By.ID,"autocomplete") #using Id selector
street1=driver.find_element(*(By.XPATH,"//input[@id='street_number']")) #using XPATH selector
street2=driver.find_element(*(By.XPATH,"//input[@id='route']"))
city=driver.find_element(By.ID, "locality")
state=driver.find_element(By.ID, "administrative_area_level_1")
zipCode=driver.find_element(By.ID, "postal_code")
country=driver.find_element(By.ID, "country")
#sending value to the address field
address.send_keys("Balaju, Kathmandu")
street1.send_keys("Street-2")
street2.send_keys("street=3")
city.send_keys("kathmandu")
state.send_keys("Bagmati")
zipCode.send_keys("2244")
country.send_keys("Nepal")
time.sleep(3)
driver.quit()