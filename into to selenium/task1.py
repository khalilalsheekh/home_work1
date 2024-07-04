from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
button = driver.find_element(By.XPATH,"//a[contains(text(),'Click Me')]")
button.click()

# Print the title
print_title = driver.find_element(By.XPATH, '//*[@id="post-4690"]/div[1]/h1')
print(print_title.text)
driver.quit()

like_button = driver.find_element(By.XPATH, "//button[@data-ulike-type='post']")







