from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://trytestingthis.netlify.app/")

driver.find_element(By.ID, "fname").send_keys("Indresh")
driver.find_element(By.ID, "lname").send_keys("Kumar")

driver.find_element(By.ID, "male").click()

dropdown = driver.find_element(By.ID, "option")
select = Select(dropdown)
select.select_by_value("option 3")

dropdown1 = driver.find_element(By.ID, "owc")
select = Select(dropdown1)
select.select_by_value("option 2")

checkbox = driver.find_element(By.NAME, "option1").click()
checkbox1 = driver.find_element(By.NAME, "option3").click()

ansGuess = driver.find_element(By.NAME, "Options")
ansGuess.send_keys("Chocolate")

pickColor = driver.find_element(By.ID, "favcolor")
pickColor.send_keys("black")

selectDate = driver.find_element(By.ID, "day")
selectDate.send_keys("18-08-2003")

scrollRange = driver.find_element(By.ID, "a")
driver.execute_script("""
    arguments[0].value = arguments[1];
    arguments[0].dispatchEvent(new Event('input'));
    arguments[0].dispatchEvent(new Event('change'));
""", scrollRange, 27)

uploadFile = driver.find_element(By.ID, "myfile")
uploadFile.send_keys("I:\\itachi.jpg")

quantityRange = driver.find_element(By.ID, "quantity")
driver.execute_script("""
    arguments[0].value = arguments[1];
    arguments[0].dispatchEvent(new Event('input'));
    arguments[0].dispatchEvent(new Event('change'));
""",quantityRange, 6)

longMessage = driver.find_element(By.NAME, "message").send_keys(" Indra love cats.")

time.sleep(7)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(3)