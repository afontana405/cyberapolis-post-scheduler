from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from login import login
from intake_data import intakeExcelSheet
from create_post import createScheduledPost

def main():

    df = intakeExcelSheet()
    
    driver = None # Initialize driver 
    try:
        driver = webdriver.Chrome()

        loggedInDriver = login(driver)

        if loggedInDriver:
            print('login successful')

        createScheduledPost(df, driver)
        
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

if __name__ == "__main__":
    main()