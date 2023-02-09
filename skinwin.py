from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\SKINWIN",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True})
driver = webdriver.Chrome(options=options)
try:
    driver.get('https://pms.ezderm.com/payments');
except:
    print("URL Issue")
try:
    username = driver.find_element(By.ID, 'username');
    username.send_keys("TrishSkinwin");
    password = driver.find_element(By.ID, 'password');
    password.send_keys("TAG123tag!");
    password.send_keys(Keys.RETURN);
except:
    print("Login Issue")
time.sleep(2)
try:
    driver.find_element(By.CSS_SELECTOR, '#root > div > div.app_ContentContainer__2meRF > div > main > div > div.cardTable_Card__GjZ22 > div:nth-child(1) > div > div.tableBase_EZTableHeader__1fkf8 > div.tableBase_Right__-q7Jz > svg:nth-child(1)').click();
except:
    print("Download Issue")
time.sleep(30)
import os
import glob
os.remove(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\SKINWIN\Payments.csv")
newest = min(glob.glob(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\SKINWIN\*"), key=os.path.getctime)
os.rename(newest, r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\SKINWIN\Payments.csv")