import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#Open and login testing site
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("nicolaika005@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

#Open the passport form
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div[1]").click()
time.sleep(2)

#Fill the pasport form
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Иванова")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Мария")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Ивановна")
time.sleep(2)
driver.find_element(By.NAME, "date").clear()
driver.find_element(By.NAME, "date").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/table/tbody/tr[2]/td[4]").click()
time.sleep(2)
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("5874")
time.sleep(2)
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys(857458)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").click()
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div/div[2]/table/tbody/tr[4]/td[3]").click()
time.sleep(2)
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys(587111)
time.sleep(2)
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys(77788899966)
time.sleep(2)
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("УФМС по Свердловской области")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+"a")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г. Ярославль")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.ARROW_DOWN)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//*[@id='phone']").click()
driver.find_element(By.XPATH,"//*[@id='phone']").send_keys(Keys.CONTROL+"a")
driver.find_element(By.XPATH,"//*[@id='phone']").send_keys(Keys.DELETE)
driver.find_element(By.XPATH,"//*[@id='phone']").send_keys("9874111147")
time.sleep(1)

#Check-box
driver.find_element(By.XPATH,"//*[@id='privacy']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='privacy']").click()

#Attachind a document to a passport form
img_input = driver.find_element(By.XPATH, "//input[@type='file']")
img_input.send_keys("D:\Рабочий стол\depositphotos_70253417-stock-photo-funny-monkey-with-a-red.jpg")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)
#open and login the administrator's site
driver.get("https://adminqa.neapro.site/login")
driver.find_element(By.ID,"admin_email").click()
driver.find_element(By.ID,"admin_email").send_keys("moderat@neapro.ru")
time.sleep(3)
driver.find_element(By.ID,"admin_password").send_keys("Aa123456")
time.sleep(3)
driver.find_element(By.NAME, "commit").click()
time.sleep(2)

#Confirmation of the document
driver.get("https://adminqa.neapro.site/users/2012")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.documents_passport').click()
driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("принят")
driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)
time.sleep(5)

#Change password
driver.get("https://qa.neapro.site/cabinet/security")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div").click()
time.sleep(2)
driver.find_element(By.ID, "oldPassword").click()
driver.find_element(By.ID, "oldPassword").send_keys("12345678")
time.sleep(2)
driver.find_element(By.ID, "newPassword").send_keys("87654321")
time.sleep(2)
driver.find_element(By.ID, "confirmPassword").send_keys("87654321")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)

#Logout
driver.set_window_size(645,612)
size = driver.get_window_size()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".mobile_menu__burger").click()
driver.find_element(By.CSS_SELECTOR, ".logout").click()

#Login with new password
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("nicolaika005@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("87654321")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

#Change password
driver.get("https://qa.neapro.site/cabinet/security")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div").click()
time.sleep(2)
driver.find_element(By.ID, "oldPassword").click()
driver.find_element(By.ID, "oldPassword").send_keys("87654321")
time.sleep(2)
driver.find_element(By.ID, "newPassword").send_keys("12345678")
time.sleep(2)
driver.find_element(By.ID, "confirmPassword").send_keys("12345678")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)

#Logout
driver.set_window_size(645,612)
size = driver.get_window_size()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".mobile_menu__burger").click()
driver.find_element(By.CSS_SELECTOR, ".logout").click()









































































































