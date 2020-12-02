"""
apt install mailutils

# Add following line to file /etc/postfix/master.cf
smtps     inet  n       -       y       -       -       smtpd
"""
import ssl
import smtplib


HOSTNAME = 'localhost'
PORT = 465


smtp = smtplib.SMTP_SSL(USERNAME, port=PORT)

context = ssl.create_default_context()

smtp.starttls(context=context)
# (220, b'2.0.0 Ready to start TLS')
