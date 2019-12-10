import smtplib
from email.mime.text import MIMEText


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'myusername@gmail.com'
SMTP_PASS = 'mypassword'

EMAIL_FROM = 'myusername@gmail.com'
EMAIL_TO = ['user1@example.com', 'user2@example.com']
EMAIL_SUBJECT = 'My Subject'
EMAIL_BODY = 'My Email Body'


msg = MIMEText(EMAIL_BODY)
msg['Subject'] = EMAIL_SUBJECT
msg['From'] = EMAIL_FROM
msg['To'] = ', '.join(EMAIL_TO)


server = smtplib.SMTP_SSL(
    host=SMTP_HOST,
    port=SMTP_PORT)

server.login(
    user=SMTP_USER,
    password=SMTP_PASS)

server.sendmail(
    from_addr=EMAIL_FROM,
    to_addrs=EMAIL_TO,
    msg=msg.as_string())

server.quit()
