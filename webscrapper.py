import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.w3schools.com/sql/'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements in the HTML using BeautifulSoup's selectors
# Example: Extract all the links from the page
links = soup.select('a')

# Iterate over the extracted links and print their text and href attribute
for link in links:
    link_text = link.text
    link_href = link.get('href')
    print(f'Text: {link_text}, Href: {link_href}')