from bs4 import BeautifulSoup

with open("dummy.html", "r") as f:
    content=f.read()#useful for when you want to read the content
    #print(content)# this is a basic string so searching and other operation is extremely hard to do
    soup=BeautifulSoup(content, 'lxml')
    #print(soup)#this is a soup object that can use methods 
    # print all h5 tags
    # tags=soup.find_all('h5')#finds the first element then stops execution,  find_all finds all the h5 tags returns a list
    # for course in tags:
    #     print(course.text)
    course_cards=soup.find_all('div', class_='card')
    for courses in course_cards:
        course_name=courses.h5.text
        course_price=courses.a.text.split()[-1]
        print(course_name+" is only "+course_price)
        

