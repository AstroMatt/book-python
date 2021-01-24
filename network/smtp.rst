****
SMTP
****


Send plaintext email
====================
.. literalinclude:: src/smtp-email-text.py
    :language: python
    :caption: Send plaintext email


Send email with attachments
===========================
.. literalinclude:: src/smtp-email-attachment.py
    :language: python
    :caption: Send email with attachments


Secured connection to the SMTP server
=====================================
.. literalinclude:: src/smtp-ssl.py
    :language: python
    :caption: Secured connection to the SMTP server


Assignments
===========

Send email
----------
* Filename: ``network/smtp.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 25 min

#. Połącz się z serwerem podanym przez prowadzącego
#. Wyślij wiadomość email na podany przez prowadzącego adres
#. Do wiadomości załącz plik ``pep20.txt``, który będzie wynikiem polecenia ``import this`` :pep:`20`
