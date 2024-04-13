import requests


# Your API KEY goes here:
api_key = 'api_key'
url = (f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-04&sortBy"
       f"=publishedAt&apiKey={api_key}")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access articles' titles
for article in content['articles']:
    print(article['title'])
    print(article['description'])
