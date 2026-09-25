import os
from bs4 import BeautifulSoup
import requests
import typing
from dotenv import load_dotenv
# from keep_alive import keep_alive

#setup to keep this running on render

#run flask ap on a seperate thread

#telegram Setup
load_dotenv()
token: typing.Final=os.getenv("TELEGRAM_TOKEN") #show a warning by text editor or ide saying can't assign another value to the variable
chat_id: typing.Final=os.getenv("MY_CHAT_ID")
username: typing.Final=os.getenv("USERNAME")




#sending message to the telegram bot
#this is for testing purpose 
# message="Hello how are you from vs code"
# url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"# f It allows you to inject Python variables directly inside a text 
#                                                                                         # string by placing them inside curly braces
# r=requests.get(url)
# print(r)


allowed_texts=['freshman','orientation']
def check_keyword(title_text) :
    return all(item in title_text for item in allowed_texts)

def check_notice_exists(notices):
     notice_text = notices
     with open ("seen_notices.txt","r") as file:
         for line in file:
             if(notice_text==line.strip()):
                 return True      
         with open("seen_notices.txt","a") as file:
                     file.write(notice_text + "\n")
         return False
             
     

def find_exam(notices):
    for n in notices:
        title_text = n.text.lower().strip()
            if check_keyword(title_text.lower().split()):
                if not check_notice_exists(title_text):  
                      url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={title_text}"
                      requests.get(url)


    
if __name__=="__main__":
    try:
        html_text=requests.get(f"https://www.aiub.edu/category/notices?pageNo=1&pageSize=20").text
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
    except Exception as e:
            print("ERROR:", e)
            
    #Reson to add try-except
    # If requests.get() tries to reach AIUB while your network disconnects 
    # for even a split second, Python will instantly throw a ConnectionError
    # and stop execution entirely. You would have to manually restart it 
    # in VS Code.
    # Resilience: 
    # If your internet connection goes down while you sleep, 
    # the script won't crash. It will hit the except block, wait 1 minute, 
    # and gracefully attempt to connect again.




