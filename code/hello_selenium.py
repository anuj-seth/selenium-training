#!/usr/bin/env python

import time

from selenium import webdriver

# Takes an optional argument, the full path to webdriver binary
#  if not specified will search path.
driver = webdriver.Chrome()  

# implicitly_wait sets a global timeout for find_element calls
# it is not the same as a time.sleep, a common misconception
driver.implicitly_wait(30)

driver.maximize_window()

# open google
driver.get("http://www.google.com")

# get the search text box
search_box = driver.find_element_by_name("q")
search_box.clear()

# send search string and submit
search_box.send_keys("python selenium")
search_box.submit()

# kids, don't try this at home
time.sleep(10)

driver.quit()

