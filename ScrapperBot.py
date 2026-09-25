import os
from bs4 import BeautifulSoup
import requests
import typing
from dotenv import load_dotenv
# from keep_alive import keep_alive

# setup to keep this running on render

# run flask app on a separate thread

# Telegram Setup
load_dotenv()

token: typing.Final = os.getenv("TELEGRAM_TOKEN")
chat_id: typing.Final = os.getenv("MY_CHAT_ID")
username: typing.Final = os.getenv("USERNAME")


# Allowed keywords
allowed_texts = ['freshman', 'orientation']

def check_keyword(title_text):
    return all(item in title_text for item in allowed_texts)


def check_notice_exists(notices):
    notice_text = notices

    with open("seen_notices.txt", "r") as file:
        for line in file:
            if notice_text == line.strip():
                return True

    with open("seen_notices.txt", "a") as file:
        file.write(notice_text + "\n")

    return False


def find_exam(notices):
    for n in notices:
        title_text = n.text.lower().strip()

        if check_keyword(title_text.split()):
            if not check_notice_exists(title_text):
                url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={title_text}"
                requests.get(url)


if __name__ == "__main__":
    try:
        html_text = requests.get(
            "https://www.aiub.edu/category/notices?pageNo=1&pageSize=20"
        ).text

        soup = BeautifulSoup(html_text, 'lxml')
        notices = soup.find_all("h2", class_="title")

        find_exam(notices)

    except Exception as e:
        print("ERROR:", e)
