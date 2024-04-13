import requests
import send_email as send
import datetime

today = datetime.date.today()

# Your API KEY goes here:
api_key = 'YOUR-API-KEY'
url = (f"https://newsapi.org/v2/everything?q=tesla&from={today}&sortBy"
       f"=publishedAt&apiKey={api_key}")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

text = ''
# Access articles' titles
for article in content['articles']:
    if article['title'] is not None:
        text = text + article['title'] + '\n' + article['description'] + 2*'\n'

text = text.encode('utf-8')
send.send_email(message=text)
