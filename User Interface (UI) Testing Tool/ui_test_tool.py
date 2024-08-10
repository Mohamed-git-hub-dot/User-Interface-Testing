from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Define a function to run a specific test case
def run_test_case(test_case_file):
    # Configure WebDriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_service = Service('path/to/chromedriver')  # Update path as needed

    # Initialize WebDriver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get('http://yourwebsite.com')  # Replace with the URL of the web application

    # Load and execute test cases
    with open(test_case_file, 'r') as file:
        exec(file.read(), {'driver': driver})

    driver.quit()

if __name__ == '__main__':
    # Directory containing test cases
    test_cases_dir = 'test_cases/'

    for test_case_file in os.listdir(test_cases_dir):
        if test_case_file.endswith('.py'):
            print(f'Running test case: {test_case_file}')
            run_test_case(os.path.join(test_cases_dir, test_case_file))
            time.sleep(2)  # Optional: wait between test cases
