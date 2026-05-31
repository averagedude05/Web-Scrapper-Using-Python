import os
import time
from bs4 import BeautifulSoup
import requests
import typing
from dotenv import load_dotenv


#telegram Setup
load_dotenv()
token: typing.Final=os.getenv("TELEGRAM_TOKEN") #show a warning by text editor or ide saying can't assign another value to the variable
chat_id: typing.Final=os.getenv("MY_CHAT_ID")
username: typing.Final=os.getenv("USERNAME")


#Webscrapper setup
seen_notices=set()


#sending message to the telegram bot
#this is for testing purpose 
message="Hello how are you from vs code"
url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"# f It allows you to inject Python variables directly inside a text 
                                                                                        # string by placing them inside curly braces
r=requests.get(url)
print(r)


#General Syntax of a genearator statement
# (expression for item in iterable if condition) 
def check_keyword(title_text) :
    return "exam" in title_text and "schedule" in title_text
def find_exam(notices):
    for n in notices:
        title_text = n.text.strip().lower()
        if check_keyword(title_text):
            if(title_text not in seen_notices):
                print(title_text)
                seen_notices.add(title_text)
    
if __name__=="__main__":
   
    while True:
        html_text=requests.get('https://www.aiub.edu/category/notices').text
        #uses a library called requests to visit the AIUB notices page.
        # It downloads the entire raw HTML source code of that webpage 
        # and saves it into a variable called html_text.
        soup=BeautifulSoup(html_text, 'lxml')
        #html_text: The raw, messy HTML text downloaded from the website.
        #'lxml': The fast "engine" (parser) that reads the HTML code and organizes it.
        #BeautifulSoup(...): The tool that blends the text and the engine together.
        # soup: The final, clean variable you can now easily search 
        # (e.g., searching for notice titles).
        notices=soup.find_all("h2", class_="title")
        find_exam(notices)
        message="Hello from vs code"
        url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        r=requests.get(url) #.get() sends the command out to the internet and brings back the server's response.
        #Why GET was used here
        #Purpose: It bundles all your data (token, chat ID, and text) directly into the web address string.
        #Reason: It is incredibly simple and quick to write. It allows you to trigger a message just by opening a single URL line.
        #Why POST is better
        #Security: POST hides your private bot token and chat ID inside the request body, keeping them out of browser histories and server logs.
        #Capacity: GET URLs break if the text message is too long (usually over 2,000 characters). POST has no size limits, allowing you to send massive messages or notices.
        time_wait=15
        time.sleep(time_wait*60)
        
        

