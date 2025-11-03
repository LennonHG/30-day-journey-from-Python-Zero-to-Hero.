import requests
from bs4 import BeautifulSoup

# Define Target URL

URL = "https://www.visayans.org"

# Fetch HTML Content

try:
    response = requests.get(URL)
    response.raise_for_status()
    html_content = response.text
except requests.RequestException as e:
    print(f"An error occur while parsing the page")
    exit()

soup = BeautifulSoup(html_content, 'html.parser')

# 4. Find and extract the page title using the <title> tag
page_title = soup.title.text

# 5. Output the result
print(f"Successfully scraped the title from the URL:")
print(f"-> {page_title}")

