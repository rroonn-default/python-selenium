from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a Service object with ChromeDriver path
service = Service(ChromeDriverManager().install())

# Launch browser using the Service object
driver = webdriver.Chrome(service=service)

# Maximize the window and open Google
driver.maximize_window()
driver.get("https://www.google.com")

# Wait a little to make sure page loads
time.sleep(2)

# Find the search box and type a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

#
