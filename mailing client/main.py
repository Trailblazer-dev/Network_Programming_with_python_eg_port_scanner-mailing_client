
import smtplib
# we using this protocol to send mails coz we need to take our script and log into an existing email account and send the mail
from email import encoders
from email.mime.text import MIMEText # this is used to send text based emails
from email.mime.base import MIMEBase # this is used to send non-text based emails e.e attachments
from email.mime.multipart import MIMEMultipart # this is used to send multi-part emails

# we are not sending email directly from the python script instead we are using the script to logging into an existing email account and sending the mail



server = smtplib.SMTP('smtp.mailgun.com',587)

server.ehlo() #this is a command that we use to start the connection


server.login('email address','password') # Don't use ur password as text instead use encrypted password


msg = MIMEMultipart()
msg['From'] = 'postmaster@sandbox13802db789414673a7351a88799ba94c.mailgun.org'
msg['To'] = 'richvictor830@gmail.com'
msg['Subject'] = 'I am your worst nightmare'


with open('mailing client/message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'mailing client/pic.jpg'
attachment = open(filename,'rb') # rb mean read binary

p = MIMEBase('application','octet-stream') # octet-stream is a generic binary file
p.set_payload(attachment.read())

encoders.encode_base64(p) # encode the attachment
p.add_header('Content-Disposition',f'attachment; filename={filename}') # this is used to add the header to the attachment

msg.attach(p) # attach the attachment to the email

text =msg.as_string() # convert the message to a string
server.sendmail('postmaster@sandbox13802db789414673a7351a88799ba94c.mailgun.org','richvictor830@gmail.com',text) # send the mail
