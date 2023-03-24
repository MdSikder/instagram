import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

# upload_files_path = os.path.join(os.path.abspath(__file__ + "/..?")),
# upload_files_path = os.path.abspath(os.path.join(os.path.abspath(__file__ + "/..?"), "")


driver = webdriver.Chrome()
# driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("https://www.instagram.com/")
# to identify element
time.sleep(5)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("usemany5@gmail.com")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwer1234!!@@")
time.sleep(20)

# driver.find_element(By.XPATH, "//button[@type='submit").click()
# time.sleep(10)
#
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
# time.sleep(3)

# driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
# time.sleep(2)


driver.find_element(By.XPATH, "//button[text()='Select from computer']").click()
# file path specified with send_keys
# s.send_keys("C:\1.png")
time.sleep(5)

pyautogui.typewrite("C:\\Users\\KloverCloud\\PycharmProjects\\project\\WebBots\\instagram\\upload\\filpng.png")
time.sleep(2)

pyautogui.press('enter')
time.sleep(3)
