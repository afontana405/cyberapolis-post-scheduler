# Import the necessary modules
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

def login(driver):
    try:
        load_dotenv()
        driver.get("https://portal.cyberapolis.com/login")
        
        usernameHTML = driver.find_element(By.ID, "Username")
        passwordHTML = driver.find_element(By.ID, "Password")
        submitBtn = driver.find_element("css selector", "input[type='submit']")

        usernameHTML.clear() 
        passwordHTML.clear()

        email = os.getenv("EMAIL", "")
        password = os.getenv("PASSWORD", "")

        usernameHTML.send_keys(email)
        passwordHTML.send_keys(password)

        submitBtn.click()

        verify(driver)

    except Exception as e:
        print(f"An error occured: {e}")

def verify(driver):
    while True:
        try:
            try: # if no code html element found, login assumed successful
                codeHTML = driver.find_element(By.ID, "Code")
            except NoSuchElementException:
                break

            submitBtn = driver.find_element("css selector", "input[type='submit']")

            codeHTML.clear()

            codeInput = input('Insert Verifcation Code (check email) if verfication code not needed leave blank and press enter:     ')
            if codeInput != "":
                codeHTML.send_keys(codeInput)
                submitBtn.click()
            else:
                continue # if no code entered, loops to start of while loop to break when no code html element found
                
            error = driver.find_element("css selector", "div.text-danger.validation-summary-errors li").text
            if "Invalid code." in error:
                continue

        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":
    driver = None # Initialize driver 
    try:
        driver = webdriver.Chrome()

        loggedInDriver = login(driver)

        if loggedInDriver:
            print('login successful')

    except WebDriverException as e:
        print(f"A WebDriver error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Step 5: Ensure the browser is closed, regardless of success or failure.
        if driver:
            input("press enter to close browser")
            driver.quit()
            print("Browser session closed.")

