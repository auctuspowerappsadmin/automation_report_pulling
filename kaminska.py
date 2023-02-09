from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import glob
import zipfile
from datetime import date
today = date.today()
tday = today.strftime("%m/%d/%Y")
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True})
driver = webdriver.Chrome(options=options)
try:
    driver.get('https://pms.ezderm.com/customReports');
except:
    print("URL Issue")
try:
    username = driver.find_element(By.ID, 'username');
    username.send_keys("TBowlby1");
    password = driver.find_element(By.ID, 'password');
    password.send_keys("TAG123tag!");
    password.send_keys(Keys.RETURN);
except:
    print("Login Issue")
time.sleep(2)
try:
    driver.find_element(By.CSS_SELECTOR, '#root > div > div.app_ContentContainer__2meRF > div > main > div > div.style_SplitView__22Y2P > div.style_col-0__3g6Go > div > div.styles_Parent__3drPb > div:nth-child(16) > div > div > div > div > div').click();
    driver.find_element(By.CSS_SELECTOR, '#paymentsDateRange').send_keys(Keys.CONTROL + "a");
    driver.find_element(By.CSS_SELECTOR, '#paymentsDateRange').send_keys('01/01/2018 - ' + tday);
    driver.find_element(By.CSS_SELECTOR, '#root > div > div.app_ContentContainer__2meRF > div > main > div > div.style_SplitView__22Y2P > div.style_col-1__2nqzi > div > div.buttonWrapper_ButtonWrapper__1gFeV > div.buttonWrapper_Right__3LXE7 > button:nth-child(1)').click();
except:
    print("Download Issue")
time.sleep(10)
os.remove(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA\Payments.csv")
list_of_files = glob.glob(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA\*")
latest_file = max(list_of_files, key=os.path.getctime)
with zipfile.ZipFile(latest_file, 'r') as zip_ref:
    zip_ref.extractall(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA")
os.remove(latest_file)
newest = min(glob.glob(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA\*"), key=os.path.getctime)
os.rename(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA\payments_allocation_custom_report.csv", r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA\Payments.csv")
os.remove(r"C:\Users\jacqu\OneDrive - The Auctus Group\Daily Client Reports\KAMINSKA\payments_allocation_summary_report.csv")