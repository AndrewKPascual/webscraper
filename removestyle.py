import re

def remove_html_tags(html):
    # Define the list of tags to exclude from removal
    excluded_tags = ['span']

    # Remove <script> tags and their contents
    html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html, flags=re.IGNORECASE)

    # Remove <meta> tags and their contents
    html = re.sub(r'<meta\b[^<]*(?:(?!<\/meta>)<[^<]*)*<\/meta>', '', html, flags=re.IGNORECASE)

    # Remove <div> tags and their contents
    html = re.sub(r'<div\b[^<]*(?:(?!<\/div>)<[^<]*)*<\/div>', '', html, flags=re.IGNORECASE)

    # Remove all other HTML tags except the excluded tags
    html = re.sub(r'<(?!\/?(?:' + '|'.join(excluded_tags) + r')(?:\s|>)).*?>', '', html)

    # Remove leading and trailing whitespaces
    html = html.strip()

    return html

def clean_html(html_file_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html = file.read()

    # Remove HTML tags
    cleaned_html = remove_html_tags(html)

    # Save the cleaned HTML to a text file
    cleaned_text_file_path = html_file_path.replace('.html', '_cleaned.txt')
    with open(cleaned_text_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_html)

    print(f"Cleaned HTML saved as text file: {cleaned_text_file_path}")

# Provide the path to the HTML file you want to clean
html_file_path = 'page_source.html'  # Update with the actual file path

# Clean the HTML file and save the cleaned content to a text file
clean_html(html_file_path)
