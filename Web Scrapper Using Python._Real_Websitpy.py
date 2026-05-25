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
html_text=requests.get('https://www.aiub.edu/category/notices?pageNo=4&pageSize=20').text
soup=BeautifulSoup(html_text, 'lxml')
seen_notices=set()



#General Syntax of a genearator statement
# (expression for item in iterable if condition) 
def check_keyword(title_text) :
    return "exam" in title_text and "schedule" in title_text
def find_exam():
    for n in notices:
        title_text = n.text.strip().lower()
        if check_keyword(title_text):
            if(title_text not in seen_notices):
                print(title_text)
                seen_notices.add(title_text)
    
if __name__=="__main__":
    while True:
        notices=soup.find_all("h2", class_="title")
        find_exam()
        time_wait=15
        print("Waiting for: ",time_wait," minutes")
        time.sleep(time_wait*60)

