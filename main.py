# Instagram scrapper
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/kc/Downloads/chromedriver')
driver.get("http://www.instagram.com")

# target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username_input = input("Enter your Instagram username: ")
username.send_keys(username_input)

password.clear()
password_input = input("Enter your Instagram password: ")
password.send_keys(password_input)

# target the login button and click it
button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# We are logged in!
