from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Chrome Driver Selenium\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get('https://www.amazon.com')
# driver.close() # it close the current active tab.
# driver.quit() # it close the entire browser.

# ----------------------------------------------------
# driver.get("https://www.python.org/")
# read = driver.find_element(By.CLASS_NAME, 'readmore')
# print(read.tag_name)
# print(driver.find_element(By.ID, 'downloads').tag_name)
# print(driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a').text)
# print(driver.find_element(By.NAME, 'q').tag_name)
# print(driver.find_element(By.CSS_SELECTOR, '.introduction a').text)

#-------------------------------------------------------
# CHALLENGE:-

# event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "name": event_names[n].text,
#         "time": event_times[n].text,
#     }
# print(events)
# ---------------------------------------------
# input_text = driver.find_element(By.NAME, 'q')
# print(input_text.get_attribute('placeholder'))
# input_text.send_keys('turtle')
# input_text.send_keys(Keys.ENTER)
# ----------------------------------------------
# CHALLENGE FILLING FORM AUTOMATICALLY.

# driver.get("https://secure-retreat-92358.herokuapp.com/")
# f_name = driver.find_element(By.NAME, "fName")
# l_name = driver.find_element(By.NAME, "lName")
# email = driver.find_element(By.NAME, "email")
# button = driver.find_element(By.CSS_SELECTOR, "form button")
# f_name.send_keys("steve")
# l_name.send_keys("smith")
# email.send_keys("steve@gmail.com")
# button.click()
# print(f_name.get_attribute("placeholder"))
# print(l_name.get_attribute("placeholder"))
# print(email.get_attribute("placeholder"))
# print(button.text)

# driver.close()