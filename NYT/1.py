from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import urllib.request
import nltk
nltk.download("stopwords")
response = urllib.request.urlopen('file:///D:/Tim%20Wu%20-%20The%20New%20York%20Times.html')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
for key, val in freq.items():
    print(str(key)+':'+str(val))
freq = nltk.FreqDist(tokens)
freq.plot(40, cumulative=False)
stopwords.words('english')
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
freq.plot(40, cumulative=False)
