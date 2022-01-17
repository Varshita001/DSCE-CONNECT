from selenium import webdriver;
from selenium.webdriver.common.keys import Keys; 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import unittest
import logging
from random import randint
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\selenium driver\chromedriver.exe")

driver.get("https://dsce-connect-website.vercel.app/index.html")
driver.maximize_window()
a = ActionChains(driver)
print(driver.title)
time.sleep(2)

#ABOUT PAGE
m = driver.find_element_by_xpath("//a[normalize-space()='ABOUT']")
a.move_to_element(m).perform()
time.sleep(0.6)
driver.find_element_by_xpath("//a[normalize-space()='ABOUT']").click()
time.sleep(5)

#NOTICES PAGE
n = driver.find_element_by_xpath("//a[normalize-space()='NOTICES']")
a.move_to_element(n).perform()
time.sleep(0.5)
driver.find_element_by_xpath("//a[normalize-space()='NOTICES']").click()
time.sleep(2)
driver.find_element_by_id("TableInput").send_keys("FIN")
time.sleep(3.7)
driver.find_element_by_xpath("//*[@id='GbpecTable']/tr[2]/td[3]/a").click()
time.sleep(2)
p= driver.window_handles[0]
#obtain browser tab window
c = driver.window_handles[1]
#switch to tab browser
driver.switch_to.window(c)
print("Page title :")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
driver.switch_to.window(p)

#EVENTS PAGE
o = driver.find_element_by_xpath("//a[normalize-space()='EVENTS']")
a.move_to_element(o).perform()
time.sleep(0.5)
driver.find_element_by_xpath("//a[normalize-space()='EVENTS']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/header/div/div/div/div[3]/div/a").click()
time.sleep(2)

#PROJECTS PAGE
p = driver.find_element_by_xpath("//a[normalize-space()='PROJECTS']")
a.move_to_element(p).perform()
time.sleep(0.5)
driver.find_element_by_xpath("//a[normalize-space()='PROJECTS']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,600)","")
time.sleep(2)
driver.execute_script("window.scrollBy(0,700)","")
time.sleep(2)

#PLACEMENT PAGE
q = driver.find_element_by_xpath("//a[normalize-space()='PLACEMENTS']")
a.move_to_element(q).perform()
time.sleep(0.5)
driver.find_element_by_xpath("//a[normalize-space()='PLACEMENTS']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)","")
time.sleep(7)

#ACADEMICS PAGE

#CONTACT PAGE
s1 = driver.find_element_by_xpath("//a[normalize-space()='CONTACT']")
a.move_to_element(s1).perform() 
time.sleep(0.5)
driver.find_element_by_xpath("//a[normalize-space()='CONTACT']").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)

#LOGIN PAGE
driver.find_element_by_xpath("//a[normalize-space()='HOME']").click()
time.sleep(2)
s = driver.find_element_by_xpath("//a[normalize-space()='LOGIN']")
a.move_to_element(s).perform() 
time.sleep(0.5)
driver.find_element_by_xpath("//a[normalize-space()='LOGIN']").click()
time.sleep(2)
def slow_type(element: WebElement, text: str, delay: float=0.3):
    """Send a text to an element one character at a time with a delay."""
    for character in text:
        element.send_keys(character)
        time.sleep(delay)
username = driver.find_element_by_xpath("//input[@placeholder='Username']")        
text = "1DS19IS104"
slow_type(username, text)       

password = driver.find_element_by_xpath("//input[@placeholder='Password']")
text = "PASSWORD"
slow_type(password, text)

time.sleep(1.5)
submit = driver.find_element_by_xpath("//input[@value='Login']")
submit.click()
time.sleep(1.5)

driver.find_element_by_xpath("/html/body/header/a/img").click()
time.sleep(5)
driver.quit()