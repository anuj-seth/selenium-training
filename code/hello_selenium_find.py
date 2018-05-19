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
search_box = driver.find_elements_by_name("q")

# class and tag are not unique
search_box_class = driver.find_elements_by_class_name("gsfi")
search_box_tag = driver.find_elements_by_tag_name("input")

search_box_css = driver.find_elements_by_css_selector("input#lst-ib")
print(search_box)
print(search_box_class)
print(search_box_tag)
print(search_box_css)

# kids, don't try this at home
time.sleep(10)

driver.quit()

