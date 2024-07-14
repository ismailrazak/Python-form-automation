import smtplib
import ssl

from django.shortcuts import render
from django.core.mail import send_mail
from email.message import EmailMessage
from decouple import config
import  smtplib
import os
def homepage(request):

    return render(request,'home.html')


def process_done(request):
    email_sender = 'ismailrazak009@gmail.com'
    email_password = config("EMAIL_HOST_PASSWORD")
    email_receiver = 'ismailrazak009@gmail.com'
    subject = ' Python (Selenium) Assignment - Mohammed ismail razak    '
    body = '''Good afternoon Sir/Maam, 
     I have completed the Python(Selenium Assignment) using Selenium for form automation and django for sending emails.
For form automation, i have used the XPATH provided by selenium to locate the input fields and enter the information using send keys() method respectively.

In django i have created a simple webpage which consists of a link when clicked on, sends the email with the screenshot attachment to the receiver.
I have used the built in class provided by django called EmailMessage which sends the mail.
I have linked the project below for evaluation.
Github project link:
The auto.py script runs the automation and saves the image.The form_automation consists of the django project.
     
With Regards,
ismail razak'''

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['cc'] = 'hr@themedius.ai'
    em['Subject'] = subject
    em.set_content(body)


    attach_path = "C:/Users/ismail/submitted.png"
    with open(attach_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attach_path)
        em.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)

    return render(request, 'process_done.html')



