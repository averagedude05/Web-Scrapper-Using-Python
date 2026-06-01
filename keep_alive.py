
#Why is Flask used here
#Flask in this project is used to 
# turn my Telegram notice bot into a web service 
# so it can run on Render’s free web service tier. 
# The Flask app provides a simple web endpoint that helps keep the bot 
# running online continuously.


#What is Flask?
#Flask is a lightweight Python web framework used to build 
# web applications, APIs, and web servers. 
# It allows Python programs to communicate with the internet 
# through HTTP requests.

from flask import Flask
from threading import Thread

#creating the flask web app("Start a tiny website")
app = Flask('')

#to make flask act like a website
@app.route('/')
def home():
    return "Bot is running"
# If someone visits your website URL
# / (homepage)
# show this message:"Bot is running"
# The / is the default homepage path in URLs.
# If someone visits the root URL → run this function(what the home function and @app.route('/') does)
def run():
    app.run(host='0.0.0.0', port=8080) 

def keep_alive():
    t=Thread(target=run)
    t.start()

