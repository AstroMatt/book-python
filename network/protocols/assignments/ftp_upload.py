""" /etc/proftpd/proftpd.conf
UseIPv6				off
PassivePorts        1024 1048
MasqueradeAddress	[YOUR PUBLIC IP ADDRESS]
"""

from ftplib import FTP


HOSTNAME = 'localhost'
USERNAME = 'myusername'
PASSWORD = 'mypassword'


with FTP(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, timeout=10) as ftp:

    with open('README.txt', mode='wb') as file:
        ftp.retrbinary('RETR README.txt', file.write)

    ftp.cwd('files')

    with open('network_ftp_upload.py', mode='rb') as file:
        ftp.storbinary('STOR network_ftp_upload.py', file)
