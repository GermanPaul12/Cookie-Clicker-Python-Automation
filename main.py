from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Applications/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()



cookie = driver.find_element(By.ID, "cookie")


product1 = driver.find_element(By.ID, "buyCursor")
product2 = driver.find_element(By.ID, "buyGrandma")
product3 = driver.find_element(By.ID, "buyFactory")
product4 = driver.find_element(By.ID, "buyCursor")
product5 = driver.find_element(By.ID, "buyMine")
product6 = driver.find_element(By.ID, "buyShipment")
product7 = driver.find_element(By.ID, "buyAlchemy lab")
product8 = driver.find_element(By.ID, "buyPortal")
product9 = driver.find_element(By.ID, "buyTime machine")


t_end = time.time() 


while time.time() < t_end + 5:
    cookie.click()
product3.click()
while time.time() < t_end + 10:
    cookie.click()
product3.click()
while time.time() < t_end + 20:
    cookie.click()
    
    
    
# driver.quit()