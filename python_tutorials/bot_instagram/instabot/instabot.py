from selenium import webdriver
import time

driver = webdriver.Safari()
driver.get("https://www.instagram.com")

time.sleep(5)

driver.quit()