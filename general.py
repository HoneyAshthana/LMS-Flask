from app import app
import smtplib
from flask_mail import Mail, Message
"""app=Flask(__name__)"""
app.config.update(
    DEBUG=True,
    #mail settings
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='honey.ashthana02@gmail.com',
    MAIL_PASSWORD='Bunny@0209',
)
mail=Mail(app)

def send_email(subject,sender,recipients,text_body,html_body):
    
        msg=Message(subject,sender="honey.ashthana02@gmail.com",recipients=["honey.ashthana02@gmail.com"])
        msg.body=text_body
        msg.html = html_body
        mail.send(msg)
        return'Mail Sent'
    
