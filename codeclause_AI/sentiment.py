from textblob import TextBlob
import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the specific paragraph you're interested in
paragraphs = soup.find_all('p')
target_paragraph = paragraphs[1] 

text = target_paragraph.text

print(text)

blob1 = TextBlob(text)
print(blob1.sentiment)
print("\n\n")

feedback = "the movie is awesome and i have fun watching it !!"
blob2 = TextBlob(feedback)
print(feedback)
print(blob2.sentiment)