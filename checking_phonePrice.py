import requests
from bs4 import BeautifulSoup
import smtplib
import time

url="https://www.trendyol.com/apple/iphone-11-64gb-beyaz-cep-telefonu-apple-turkiye-garantili-aksesuarsiz-kutu-p-65149494"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}


def check_info():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    prod_name = soup.find("h1", attrs={"class": "pr-new-br"}).span.get_text()
    print(prod_name)

    price = soup.find("span", attrs={"class": "prc-dsc"}).get_text().split()[0]
    price = float(price)*1000
    print(price)
    if price <= 11000:
        send_mail(prod_name)

def send_mail(prod_name):
    sender = "codingwithpython3@gmail.com"
    receiver = "mehmetdora333@gmail.com"


    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(receiver, "19460083270Qaz")

    subject = "ÜRÜN KONTROL"
    message=  prod_name + "ÜRÜNÜ 11000 TL ALTINA DÜŞMÜŞTÜR."
    content = "Subject: {}\n\n{}".format(subject, message).encode("utf-8")
    mail.sendmail(sender, receiver, content)
    print("mail gönderildi!")

while True:
    check_info()
    time.sleep(3600*6) # 6 saatte bir kontrol ediyor

