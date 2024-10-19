import requests
import smtplib
from email.mime.text import MIMEText #for sending plain text email
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def check_website(url):
    try:
        response = requests.get(url) #making GET request
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def send_email(sender_email, receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Start TLS encryption 
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit() # Close the connection
        print("Email sent successfully")
    except:
        print("Failed to send the email")


if not check_website("https://fakestoreapi.com"):
    subject = 'website is not working'
    body='application is in a terminated state'
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("APP_PASSWORD")
    receiver_email= os.getenv("RECEIVER_EMAIL")
    send_email(sender_email,receiver_email,subject,body)
else:
    print("website is up")

