from selenium import webdriver
 

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_key('hello world') 
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()
