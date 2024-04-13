# What is this project about
This app accesses news for Tesla and sends them by email.

### How to use it
In order to use this app, you must get access to your API Key by logging into
https://newsapi.org/

If you want news about other topic, feel free to browse for more in the url
provided, but you must change the variable named 'url' in main.py.

You must enter your API Key into the variable 'api_key' in main.py.

In addition, you must get the gmail accounts you want to use as sender and
receiver. For the app to use your sender email, you must generate an app 
password in your gmail account and enter it in the 'password' variable inside 
send_email.py.

Your email password is NOT your app password.
