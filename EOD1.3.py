from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import schedule

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://ads.pacificoffice.com/generic/main.cgi")

search = driver.find_element("name","user")
# Enter Username Below
search.send_keys("****")
time.sleep(1)
search = driver.find_element("name","passwd")
# Enter Password Below
search.send_keys("******")
time.sleep(1)
search = driver.find_element(By.XPATH,"/html/body/form/p/table/tbody/tr[5]/td/input").click()
search = driver.find_element(By.XPATH,"/html/body/ol/li[4]/a").click()
search = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[7]/td[2]/input")
search.send_keys("8")
search = driver.find_element(By.XPATH,"/html/body/form/input[3]").click()
time.sleep(1)
driver.close()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


 