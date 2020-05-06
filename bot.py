from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
import configparser
import sys

# ---------- Settings --------------- #
loginWithFB = True if sys.argv[1] == '1' else False
print(sys.argv[1], loginWithFB)
config = configparser.ConfigParser()
config.read('settings.ini')
driver_path = config['Settings']['PathToChromeDriver']
input_file = config['Settings']['Filename']
username = config['Settings']['FBUsername'] if loginWithFB else config['Settings']['InstaUName']
password = config['Settings']['FBPassword'] if loginWithFB else config['Settings']['InstaPassword']
user_id = config['Settings']['InstagramUserID']

# ---------- End Of Settings --------------- #

driver = webdriver.Chrome(driver_path)
wait = WebDriverWait(driver, 10)

driver.get("https://www.instagram.com/direct/inbox/")

# Login 
if loginWithFB:
	wait.until(expect.visibility_of_element_located((By.CSS_SELECTOR , ".KPnG0"))).click()
	driver.find_element_by_name("email").send_keys(username)
	driver.find_element_by_name("pass").send_keys(password)
	driver.find_element_by_name("pass").send_keys(Keys.RETURN)
else:
	wait.until(expect.visibility_of_element_located((By.NAME , "username"))).click()
	driver.find_element_by_name("username").send_keys(username)
	wait.until(expect.visibility_of_element_located((By.NAME , "password"))).click()
	driver.find_element_by_name("password").send_keys(password)
	driver.find_element_by_name("password").send_keys(Keys.RETURN)

# Click on Not Now for notification pop-up
wait.until(expect.visibility_of_element_located((By.CSS_SELECTOR , ".aOOlW.HoLwm"))).click()

# Click on the user
xpath = "//*[contains(text(),'"+user_id+"')]"
wait.until(expect.visibility_of_element_located((By.XPATH , xpath))).click()

# Send messages word-by-word
with open(input_file,'r') as file:
	msg_input = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
	for line in file:
		for word in line.split():
			msg_input.send_keys(word)
			msg_input.send_keys(Keys.RETURN)
