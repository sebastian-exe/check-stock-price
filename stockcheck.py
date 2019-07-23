#adding time and simple main transfer protocol
import time
import smtplib
#adding in the pip install from yahoo
from yahoo_fin import stock_info as si

#time successfully works, now will add a timer to check the price of these stocks
#a few times a day and to notify me once the price reaches the targeted price

print("apple")
print(si.get_live_price("aapl"))

print("amazon")
print(si.get_live_price("amzn"))

#define the price
applePrice = si.get_live_price("aapl")

#function to check the price
def check_price():
        if(applePrice = 218):
            send_mail()

#define the server function to send the sendMail
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #encripts the connection
    server.starttls()

    server.login('sebamoreno17@gmail.com','#enter password for email#')

    subject = 'target price reached.'
    body = 'buy more stock!'
    msg = f"Subject: {subject}\n\n{body}"

    #the first parameter is the sender and the second parameter is the recipient.
    #The third parameter is the message
    server.sendmail('sebamoreno17@gmail.com',
    'sebamoreno17@gmail.com',
    msg)
    print("email has been sent!")
    server.quit()


while(True):
    check_price()
    time.sleep(60)
