import openai
import requests
from bs4 import BeautifulSoup
import os
import sys  # Import the sys module for encoding handling
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

# Step 5: Estimate the token count
total_tokens = len(combined_text.split())

# Step 6: Reduce the length of the text to fit within the token limit
max_tokens = 4096 - 40  # Subtract the token count of system and user messages

if total_tokens > max_tokens:
    # Truncate the text to fit within the token limit
    tokens = combined_text.split()[:max_tokens]
    combined_text = ' '.join(tokens)

# Step 7: Use OpenAI to generate the summary
openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an AI that is going to give a summary of the text that is not HTML code inside of a website's HTML code."},
        {"role": "user", "content": combined_text}
    ],
    max_tokens=max_tokens,  # Limit the total tokens to the adjusted limit
    temperature=0.1  # Set temperature to 0.3
)

# Step 8: Extract the generated summary from the response
summary = response.choices[0].message.content

# Step 9: Save the summary to a text file
with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary.strip())

# Print the HTML content with proper encoding
print(html_content.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
