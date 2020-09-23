from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = Options()

while True:
    driver = webdriver.Chrome(
        chrome_options = chrome_options,
        executable_path = "./chromedriver.exe"
    )

    driver.maximize_window()

    driver.get("https://www.hotstar.com/us")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//IMG[@class='brand-logo hotstar-logo']/../../../../../../..//SPAN[@class='watch-now-txt'][text()='WATCH NOW'][text()='WATCH NOW'][text()='WATCH NOW'])[1]"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//H1[@class='loginFormHeader'][text()='Log In']/..//DIV[@class='link'][text()='Create Account']"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//H1[@class='loginFormHeader'][text()='Create Account']/..//INPUT[@id='fullname']"))
    )
    element.send_keys("Steven Smith")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//H1[@class='loginFormHeader'][text()='Create Account']/..//INPUT[@id='email']"))
    )
    element.send_keys("username+{}@gmail.com".format(str(time.time()).split(".")[0]))

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//H1[@class='loginFormHeader'][text()='Create Account']/..//INPUT[@id='password']"))
    )
    element.send_keys("superSimpleP@ssword123")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//H1[@class='loginFormHeader'][text()='Create Account']/..//BUTTON[@type='submit'][text()='Create Account']"))
    )
    element.click()

    time.sleep(300)

    driver.quit()
