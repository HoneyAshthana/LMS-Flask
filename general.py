# Import smtplib for the actual sending function
import smtplib
# Import email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
print("SDF")
"""yet to do"""
def send_email(toaddr, subject, body):
    """Send email"""
    fromaddr = "honey.ashthana02@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com: 587')

    msg = MIMEMultipart()
    text= 'Hey'
    print("GFDD")
    msg['From'] = fromaddr
    msg['To'] = 'honey.ashthana02@gmail.com'
    msg['Subject'] = subject

    """if ccaddr is not None:
        rcpt = ccaddr + [toaddr]
        msg['Cc'] = ", ".join(ccaddr)
    else:"""
    rcpt = toaddr

    html = """\
    <html>
      <font face="arial" size="2"> {body}
      </font>
    </html>""".format(body=body)

    msg.attach(MIMEText(html, 'html'))
    print(text)
    server.starttls()
    server.login(fromaddr, "Bunny@0209")
    text = msg.as_string()
    server.sendmail(fromaddr, rcpt, text)
    server.quit()
send_email('honey.ashthana02@gmail.com','dfghjk','dfgghjklhjk')









"""from app import app
import smtplib
from flask_mail import Mail, Message

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
        return'Mail Sent"""
    
