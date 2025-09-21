# Import the necessary modules
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

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
            codeHTML = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "Code"))
            )
            submitBtn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

            codeHTML.clear()

            codeInput = input('Insert Verification Code (check email) or press Enter if not needed: ')
            if codeInput != "":
                codeHTML.send_keys(codeInput)
                submitBtn.click()
            else:
                print("No verification code entered. Assuming login is successful.")
                break

            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.text-danger.validation-summary-errors"))
                )
                print("Invalid code. Please try again.")
            except TimeoutException:
                print("Code submitted successfully. Login completed.")
                break

        except TimeoutException:
            print("No verification page found or login was successful.")
            break
        
        except Exception as e:
            print(f"An unexpected error occurred in the verify function: {e}")
            break


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

