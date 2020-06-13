from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


url = ''
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)

launchEarthButoon = wait.until(EC.element_clickable(By.XPATH,''))