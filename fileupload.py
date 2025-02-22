#script to upload a file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#setting driver to install drivermanager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# storing url to a variable
url="https://formy-project.herokuapp.com/fileupload"
driver.get(url)
#maximize window
driver.maximize_window()
time.sleep(2)
#find file upload field
filechose=driver.find_element(By.ID, "file-upload-field")
#send file location or path
filechose.send_keys(r"C:\Users\Bhabisara Budhathoki\Pictures\Screenshots\3d rotation output.png")

time.sleep(2)
# to reset file field
reset=driver.find_element(*(By.XPATH,"//button[normalize-space()='Reset']"))
reset.click()
time.sleep(2)
driver.quit()