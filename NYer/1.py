from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import urllib.request
import nltk
nltk.download("stopwords")
url_list = ["https://www.newyorker.com/contributors/tim-wu","https://www.newyorker.com/contributors/tim-wu/page/2","https://www.newyorker.com/contributors/tim-wu/page/3","https://www.newyorker.com/contributors/tim-wu/page/4","https://www.newyorker.com/contributors/tim-wu/page/5","https://www.newyorker.com/contributors/tim-wu/page/6"]
text = ""
for i in url_list:
    response = urllib.request.urlopen(i)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    t = soup.get_text(strip=True)
    text = text + t
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
