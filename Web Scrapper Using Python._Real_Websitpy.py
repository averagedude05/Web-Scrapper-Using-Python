from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.aiub.edu/category/notices').text
soup=BeautifulSoup(html_text, 'lxml')
notices=soup.find_all("h2", class_="title")

#General Syntax of a genearator statement
# (expression for item in iterable if condition) 
def check_keyword(title_text) :
   words_intitle=title_text.split() 
   has_exam_routine= "exam" in title_text and "routine" in title_text
   if has_exam_routine:
       exam_type_and_dept= "mid" in title_text or "final" in title_text and "fst" in title_text
       
       return exam_type_and_dept
for n in notices:
    title_text = n.text.strip().lower()
   
    if check_keyword(title_text):
        print(title_text)
      
 

