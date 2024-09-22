import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.find_element(By.XPATH(//input[@name]='btnK')).click()
#driver.get("https://www.instagram.com/accounts/login/?hl=en/")
# Login #
driver.find_element(By.NAME, "username").send_keys("")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
# Password #
driver.find_element(By.NAME, "Passwd").send_keys("Lakshman@5056")
driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
# Next Page #
#driver.find_element(By.XPATH, "//span[normalize-space()='Continue']").click()
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
