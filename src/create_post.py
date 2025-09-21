import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

def createScheduledPost(df, driver):
    for index, row in df.iterrows():
        IDInput = row['ID']
        postInput = row['Post']
        dateTimeInput = f'{row['Date'].date()} {row['Time']}'

        botProfilePage = f'https://portal.cyberapolis.com/people/bot-profile/{IDInput}'
        driver.get(botProfilePage)
    
        print(IDInput, postInput, dateTimeInput)

        