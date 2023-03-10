
import time
import pickle
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


df_final = pd.DataFrame()

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()))

s = 25

for i in range(s, s+1):
    driver.get(
        'https://www.pkwteile.de/ersatzteil/bremsscheiben/232-gelocht-val-2?page='+str(i))

    # Wait before finding the accept button
    time.sleep(3)
    # Accept cookies

    consent = driver.find_element(
        by=By.XPATH, value='/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[2]/a[3]')
    consent.click()

    # dia = driver.find_elements(by=By.XPATH, value="//body//div[@id='wrapper']//div[contains(@class,'js-listing-wrap')]//div[contains(@class,'js-listing-wrap')]//div[2]//div[1]//div[3]//div[3]//ul[1]//li[2]//span[1]")

    left = driver.find_elements(by=By.CLASS_NAME, value='lc')
    right = driver.find_elements(by=By.CLASS_NAME, value='rc')

    data = []
    row = {}
    for l, r in zip(left, right):
        # Get the text from the left and right elements
        l_text = l.text
        r_text = r.text

        if l_text in row:
            data.append(row)
            row = {}
        else:
            row[l_text] = r_text

    # This is required to append the last row
    if len(row) > 0:
        data.append(row)

    # Create the dataframe from the list of dictionaries
    df = pd.DataFrame(data)
    try:
        df = df.drop([""], axis=1)
    except:
        pass
    df = df.dropna(how="all", axis=0)

    driver.close()

df_final = pd.concat([df_final, df], join="outer", axis=0, ignore_index=True)
