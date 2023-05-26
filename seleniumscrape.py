from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the Selenium Chrome driver
service = Service(r'C:\Users\andre\Desktop\chromedriver\chromedriver.exe')  # Replace with the path to your chromedriver executable
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode, no GUI
driver = webdriver.Chrome(service=service, options=options)

# Load the website
driver.get('https://www.stack-ai.com/')  # Replace with the URL of the website you want to scrape

# Wait for the dynamic content to load (you may need to adjust the wait time)
time.sleep(5)  # Adjust the delay as needed (in seconds)

# Get the page source (HTML code) after the dynamic content has loaded
page_source = driver.page_source

# Write the page source to a file
with open('page_source.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

# Close the driver
driver.quit()
