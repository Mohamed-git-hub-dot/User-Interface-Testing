from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_example(driver):
    # Example test case
    search_box = driver.find_element(By.ID, 'search')
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.RETURN)

    # Add assertions or checks here
    assert 'Selenium' in driver.title

    # Optional: take a screenshot
    driver.save_screenshot('screenshot.png')
