import requests #requests info from a website

html_text=requests.get('https://bdjobs.com/h/jobs?qOT=&txtsearch=python&lang=en').text
print(html_text)
