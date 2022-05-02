import smtplib

subject = "test"
message= "bu bir test mailidir."
content = "Subject: {}\n\n{}".format(subject,message).encode("utf-8")

#hesap bilgileri
mail= smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()

mail.starttls()

mail.login("mehmetdora333@gmail.com","19460083270Qaz")

mail.sendmail("codingwithpython3@gmail.com","mehmetdora333@gmail.com",content)
