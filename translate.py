import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()

options.add_argument('--disable-dev-shm-usage')
options.add_argument('--incognito')
lang_code = 'es'
org_txt = 'how are you'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
driver.get('https://translate.google.com/?sl=en&tl='+lang_code+'&op=translate')
driver.find_elements(By.XPATH,'/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')[0].send_keys(org_txt)
time.sleep(5)
trans_txt = driver.find_elements(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[1]/div[6]/div/div[1]/span[1]/span/span')[0].text

print(trans_txt)

driver.close()
