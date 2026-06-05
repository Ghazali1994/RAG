import requests
from bs4 import BeautifulSoup

url = "https://www.tn.gov.in"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text()

with open("tn_data.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved")
