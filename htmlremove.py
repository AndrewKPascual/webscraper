import re

def remove_css(html):
    # Remove style tags and their contents
    html = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', html, flags=re.IGNORECASE)
    
    # Remove inline style attributes
    html = re.sub(r'style\s*=\s*".*?"', '', html, flags=re.IGNORECASE)
    
    return html

def clean_html(html_file_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html = file.read()

    # Remove CSS styles
    cleaned_html = remove_css(html)

    # Save the cleaned HTML to a text file
    cleaned_text_file_path = html_file_path.replace('.html', '_cleaned.txt')
    with open(cleaned_text_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_html)
    
    print(f"Cleaned HTML saved as text file: {cleaned_text_file_path}")

# Provide the path to the HTML file you want to clean
html_file_path = 'page_source.html'  # Update with the actual file path

# Clean the HTML file and save the cleaned content to a text file
clean_html(html_file_path)
