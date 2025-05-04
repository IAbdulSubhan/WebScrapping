# 🧠 Concepts Covered
# 🧩 Element Locating
# By ID: driver.find_element(By.ID, "login_field")

# By XPath: For elements without an id or name.

# 🧠 Text Input and Clearing Fields
# Text Input: Use .send_keys("your_text") to type into input fields.

# Clearing Fields: Use .clear() before sending keys if needed.

 
# field = driver.find_element(By.ID, "example")
# field.clear()
# field.send_keys("text here")
# 🧠 Clicking Buttons or Links
# Use .click() to simulate button or link clicks.

 
# submit_button = driver.find_element(By.XPATH, "xpath_here")
# submit_button.click()
# 🧠 Form Submission
# Clicking a button within a <form> element often triggers a submit.

# .submit() is rarely needed; .click() is commonly enough.

# 📝 Best Practices
# Use descriptive locators like By.ID or By.NAME when possible.

# For dynamic sites or sensitive logins, prefer WebDriverWait instead of time.sleep().

# Never store real passwords in scripts. Use environment variables or secret managers in secure automation.

# 🔚 Ending the Script
 
# driver.quit()
# Always close the browser to release system resources.



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://github.com/login'
driver.get(url)
time.sleep(2)

# username field
username_field = driver.find_element(By.ID, 'login_field')
username_field.send_keys('misbah')
time.sleep(1)

# password field
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('pass123')
time.sleep(1)

# submit button
submit_button = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
submit_button.click()
time.sleep(2)

driver.quit()