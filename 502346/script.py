from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# This is your specific folder path
base = "file:///C:/Users/ELCOT/502346/"

try:
    # Test 1: Home Page
    driver.get(base + "index.html")
    print("Home Page Title:", driver.title)
    time.sleep(1)

    # Test 2: About Page
    driver.get(base + "about.html")
    print("About Page Loaded")
    time.sleep(1)

    # Test 3: Contact Form
    driver.get(base + "contact.html")
    driver.find_element(By.ID, "name").send_keys("Sakima")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    print("Form filled successfully!")
    time.sleep(2)

finally:
    driver.quit()
    print("Testing Finished Successfully.")
# Change this:
driver.quit()

# To this (add a #):
# driver.quit()