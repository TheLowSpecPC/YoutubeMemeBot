from time import sleep
import config,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
import undetected_chromedriver as uc

def chrome():
    a=0
    down = str(Path.home()/"Downloads")
    while(a==0):
        try:
            # Login
            driver = uc.Chrome(use_subprocess=True)
            driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            sleep(1)
            mail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "identifier")))
            mail.send_keys(config.gmail)
            driver.find_element("id", "identifierNext").click()
            sleep(1)
            passwd = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Passwd")))
            passwd.send_keys(config.password)
            driver.find_element("id", "passwordNext").click()
            sleep(2)

            # Upload
            driver.get(config.upload_button)
            sleep(2)
            driver.find_element(By.NAME, "Filedata").send_keys(down+"\\"+config.name)
            sleep(60)
            notkids = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")))
            notkids.click()
            sleep(1)
            next1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
            next1.click()
            sleep(1)
            next2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
            next2.click()
            sleep(1)
            next3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next-button")))
            next3.click()
            sleep(1)
            driver.find_element(By.NAME, "PUBLIC").click()
            sleep(1)
            done = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "done-button")))
            done.click()
            sleep(5)
            a+=1
        except:
             print("Error")
    return "Finished Uploading"