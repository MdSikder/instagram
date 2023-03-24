import time
import os
from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
import pyautogui

# Locators
from selenium.webdriver.support.wait import WebDriverWait

username = "//input[@name='username']"
password = "//input[@name='password']"
submit = "//button[@type='submit']"
Create_button = "//html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]"
upload_button = "//button[contains(text(),'Select from computer')]"
next_button = "//div[contains(text(),'Next')]"
share_button = "//div[contains(text(),'Share')]"
notification = "//button[contains(text(),'Not Now')]"

fil = "//button[text()='Select from computer']"

write = "//div[@aria-label='Write a caption...']"

driver = webdriver.Chrome()
# driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("https://www.instagram.com/")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("usemany5@gmail.com")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwer1234!!@@")
time.sleep(2)

driver.find_element(By.XPATH, submit).click()
time.sleep(20)

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# create = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, Create_button)))
try:
    # create.click()
    driver.find_element(By.XPATH, Create_button).click()
    time.sleep(5)

except NoSuchElementException as e:
    print("NoSuchElementException error :\n", e, "\n")
except TimeoutException as e:
    print("TimeoutException error", e)
except InvalidSessionIdException as e:
    print("InvalidSessionIdException", e)

driver.find_element(By.XPATH, "//button[text()='Select from computer']").click()
time.sleep(5)

pyautogui.typewrite("C:\\Users\\KloverCloud\\PycharmProjects\\project\\WebBots\\instagram\\upload\\filpng.png")
time.sleep(2)

pyautogui.press('enter')
time.sleep(3)

driver.find_element(By.XPATH, next_button).click()
time.sleep(2)

driver.find_element(By.XPATH, next_button).click()
time.sleep(3)

driver.find_element(By.XPATH, write).send_keys('hello dear window')
time.sleep(5)

driver.find_element(By.XPATH, share_button).click()
time.sleep(30)
