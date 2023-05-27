import openai
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv() 
# Step 2: Load the HTML content
with open('page_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 3: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
sections = soup.find_all('div', {'class': 'content'})

# Step 4: Prepare the text for processing by OpenAI
combined_text = '\n'.join([section.get_text() for section in sections])

# Step 5: Use OpenAI to generate the summary
openai.api_key = os.getenv('OPENAI_API_KEY')
summary = openai.Completion.create(
    engine='text-davinci-003',
    prompt=combined_text,
    max_tokens=500  # Adjust the token limit as needed
)

# Step 6: Save the summary to a text file
with open('summary.txt', 'w') as file:
    file.write(summary.choices[0].text.strip())
