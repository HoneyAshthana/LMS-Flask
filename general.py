# Import smtplib for the actual sending function
import smtplib
# Import email modules
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
"""yet to do"""
def send_email(toaddr, ccaddr, subject, body, file):
    """Send email"""
    fromaddr = "FROM_EMAIL_ADDRESS"
    server = smtplib.SMTP('SERVER_IP', PORT_NUMBER)

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    if ccaddr is not None:
        rcpt = ccaddr + [toaddr]
        msg['Cc'] = ", ".join(ccaddr)
    else:
        rcpt = toaddr

    html = """\
    <html>
      <font face="arial" size="2"> {body}
      </font>
    </html>""".format(body=body)

msg.attach(MIMEText(html, 'html'))

server.starttls()
server.login(fromaddr, "PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, rcpt, text)
server.quit()










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
    
