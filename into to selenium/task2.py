from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/complicated-page")
buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'Button')]")
count_buttons = len(buttons)
if count_buttons == 12:
    print("Test pass")
else:
    print("Test fail")

