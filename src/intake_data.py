import os
import pandas as pd

from create_post import createScheduledPost
def intakeExcelSheet():
    """
    Prompts the user for a full file path to an Excel sheet,
    reads the data into a pandas DataFrame, and returns it.
    """
    while True:
        try:
            # filePath = input("Enter full path to your Excel file: ")
            filePath = r"C:\Users\14022\Desktop\test.xlsx" # hard coded path to be deleted when testing over
            
            # Check if the file exists before attempting to read it
            if not os.path.exists(filePath):
                print("Error: File not found. Please check the path and try again.")
                continue

            df = pd.read_excel(filePath)
            return df
        
        except ValueError as e:
            # Handle cases where the input path might be a directory or non-Excel file
            print(f"Error reading file: {e}. Please ensure the file is a valid Excel spreadsheet.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    # This block will only run when you execute this script directly
    try:
        df = intakeExcelSheet()
        
        if df is not None:
            print("\nSuccessfully loaded Excel sheet into a DataFrame:")
            print("-" * 30)
            print(df.head())
            print("-" * 30)
            print("DataFrame created successfully.")
    except Exception as e:
        print(f"An error occurred while running the example: {e}")