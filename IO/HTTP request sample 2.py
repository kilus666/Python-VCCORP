from bs4 import BeautifulSoup
import requests

source= requests.get('https://tinhte.vn/threads/cam-nhan-john-wick-3-hoan-toan-xung-dang-voi-mong-doi.2961505/').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())


paragraphs= soup.find_all()
for i in paragraphs:
    print(i.text)



# partitions= soup.find("title").text
# print(partitions)
# for i in partitions:
#     print(i)


