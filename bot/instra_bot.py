from pom.locators2 import Locator
import time
import os
from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
import pyautogui


def test_SB_default_01():
    UploadFilePath = "C:\\Users\\KloverCloud\\PycharmProjects\\project\\WebBots\\instagram\\upload\\filpng.png"
    text = "hello dear window"

    driver = webdriver.Chrome()
    # driver.implicitly_wait(0.5)
    driver.maximize_window()

    driver.get("https://www.instagram.com/")
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("usemany5@gmail.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwer1234!!@@")
    time.sleep(2)

    driver.find_element(By.XPATH, Locator.submit).click()
    time.sleep(20)

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # create = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, Create_button)))
    try:
        # create.click()
        driver.find_element(By.XPATH, Locator.Create_button).click()
        time.sleep(5)

    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)

    driver.find_element(By.XPATH, Locator.selectfrom_Computer).click()
    time.sleep(5)

    pyautogui.typewrite(UploadFilePath)
    time.sleep(2)

    pyautogui.press('enter')
    time.sleep(3)

    driver.find_element(By.XPATH, Locator.next_button).click()
    time.sleep(2)

    driver.find_element(By.XPATH, Locator.next_button).click()
    time.sleep(3)

    driver.find_element(By.XPATH, Locator.write).send_keys(text)
    time.sleep(5)

    driver.find_element(By.XPATH, Locator.share_button).click()
    time.sleep(30)
#
