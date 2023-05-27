import html2text

# Read the HTML file
with open('page_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Convert HTML to Markdown
markdown_content = html2text.html2text(html_content)

# Save the Markdown content to a file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(markdown_content)
