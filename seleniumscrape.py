from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up the Selenium Chrome driver
service = Service('/path/to/chromedriver')  # Replace with the path to your chromedriver executable
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode, no GUI
driver = webdriver.Chrome(service=service, options=options)

# Load the website
driver.get('https://langlabs.io/')

# Wait for the dynamic content to load (you may need to adjust the wait time)
driver.implicitly_wait(5)  # Waits for 5 seconds

# Extract the desired information
element = driver.find_element(By.XPATH, '//some/xpath')
# Process or print the element's text or attribute as needed

# Close the driver
driver.quit()
