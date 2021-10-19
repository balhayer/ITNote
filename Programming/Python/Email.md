# Email using smtplib
## Simple Version
```python
import smtplib

recipient='user@domain.com'
cc=''
sender='sender@domain.com'
server='smtp.domain.com'
subject='Backup Report'
message='This is test message'

header='From: %s\n' % sender
header+='To: %s\n' % recipient
header+='CC: %s\n' % cc
header+='Subject: %s\n\n' % subject
message = header + message

connection = smtplib.SMTP(server)
result = connection.sendmail(sender,recipient,message)
connection.quit()
print(result)
```

## With Attachment
```Python
import email, smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "user@domain.com"
receiver_email = "user@domain.com"
server="smtp.domain.com"
#password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "T4.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header("Content-Disposition","attachment", filename=filename)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Send mail without authentication
server=smtplib.SMTP(server)
result = server.sendmail(sender_email, receiver_email, text)
print result
```

## With Attachment and Authentication
```Python
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "user@domain.com"
receiver_email = "user@domain.com"
server="smtp.domain.com"
#password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["CC"] = cc_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "T4.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header("Content-Disposition","attachment", filename=filename)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
```

## Another Version
```Python
With smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    
    subject='Some Subject'
    body='Body'
    msg=f'Subject: {Subject} \n\n {body}'
    
    smtp.sendmail(EMAIL_ADDRESS, 'RECIPIENT@GMAIL.com',msg)
```

## Example to send Backup Report
```Python
#!/usr/bin/python
import os,glob,smtplib

recipient='user@domain.com'
cc=''
sender='sender@domain.com'
server='smtp.domain.com'
subject=' Backup Report'


def report(message):
        header='From: %s\n' % sender
        header+='To: %s\n' % recipient
        header+='CC: %s\n' % cc
        header+='Subject: %s\n\n' % subject
        message = header + message

        connection = smtplib.SMTP(server)
        result = connection.sendmail(sender,recipient,message)
        connection.quit()
        return result


folder="/ConfigurationArchive/Firewall"
items=['fw01a','fw01b','fw02a','fw02b','fwmg']
listoffiles=[]
message=''
for i in items:
        files = sorted(glob.glob(folder+"/*"+i+"*"), key=os.path.getctime)
        if len(files) > 0:
                    listoffiles.append(files[-1])
for f in listoffiles:
        message=message + f.split("/")[-1] + "\n"

print report(message)
```

# Reference

- https://realpython.com/python-send-email/
- http://rosettacode.org/wiki/Send_email#Python
- http://www.blog.pythonlibrary.org/2013/06/26/python-102-how-to-send-an-email-using-smtplib-email/