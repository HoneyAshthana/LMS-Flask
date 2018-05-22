# Import smtplib for the actual sending function
import smtplib
# Import email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(toaddr, subject, body):
    """Send email"""
    fromaddr = "honey.ashthana02@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com: 587')
    text='Hey u'
    msg = MIMEMultipart()
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
#send_email('honey.ashthana02@gmail.com','dfghjk','dfgghjklhjk')



"""function that will send the user’s files directly into our bucket.
    using boto3’s Client.upload_fileobj method for this.
    Args:
        a file object
        a bucket name and 
        an optional acl keyword argument
"""
"""
def upload_file_to_s3(file, bucket_name, acl="public-read"):

    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"], file.filename)
"""

""" in addition to ACL we set the ContentType key in ExtraArgs to the file’s content type. 
This is because by default, all files uploaded to an S3 bucket have their content type set 
to binary/octet-stream, forcing the browser to prompt users to download the files instead of just
 reading them when accessed via a public URL"""


 