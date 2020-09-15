import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXCK8S6/ref=lp_21837417031_1_1?s=electronics&ie=UTF8&qid=1597426596&sr=1-1'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

def check_price():
    page= requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title=soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    new_price=price[2:8]
    x =int((new_price.replace(',','')))
    print(title.strip())
    print(f'Rs {x}')
    if(x<50000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ankitkanojiya3103@gmail.com','nnreznsueplqvztq')

    subject = 'price within budget'
    body = 'checkout the link https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXCK8S6/ref=lp_21837417031_1_1?s=electronics&ie=UTF8&qid=1597426596&sr=1-1'

    msg= f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'ankitkanojiya3103@gmail.com',
        'iamkanojiya@gmail.com',
        msg
    )

    print("msg sent successfully")
    server.quit()

i=100
while(i>0):
    i-=1
    check_price()
    time.sleep(60*60*24)
