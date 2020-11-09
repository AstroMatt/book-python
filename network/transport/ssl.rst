***
SSL
***


Socket creation
===============

Client socket example with default context and IPv4/IPv6 dual stack
-------------------------------------------------------------------
.. code-block:: python

    import socket
    import ssl


    hostname = 'www.python.org'
    context = ssl.create_default_context()


    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(ssock.version())


Client socket example with custom context and IPv4
--------------------------------------------------
.. code-block:: python

    import socket
    import ssl


    hostname = 'www.python.org'

    # PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('path/to/cabundle.pem')


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(ssock.version())

Server socket example listening on localhost IPv4
-------------------------------------------------
.. code-block:: python

    import socket
    import ssl


    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(('127.0.0.1', 8443))
        sock.listen(5)

        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            ...

SSLSocket
=========
* Passing a non-zero flags argument is not allowed
* but os.sendfile will be used for plain-text sockets only, else send() will be used

.. csv-table:: SSLSocket API
    :header-rows: 1

    "Method", "Description"
    "``accept()``", ""
    "``bind()``", ""
    "``close()``", ""
    "``connect()``", ""
    "``detach()``", ""
    "``fileno()``", ""
    "``getpeername()``", ""
    "``getsockname()``", ""
    "``getsockopt()``", ""
    "``setsockopt()``", ""
    "``gettimeout()``", ""
    "``settimeout()``", ""
    "``setblocking()``", ""
    "``listen()``", ""
    "``makefile()``", ""
    "``recv()``", ""
    "``recv_into()``", ""
    "``send()``", ""
    "``sendall()``", ""
    "``sendfile()``", ""
    "``shutdown()``", ""

.. code-block:: python

    import socket
    import ssl

    context = ssl.SSLContext()
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
    ssl_sock.connect(('www.verisign.com', 443))


Client-side operation
=====================
.. code-block:: python

    import ssl
    from pprint import pprint

    context = ssl.create_default_context()

    context = ssl.SSLContext()
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_verify_locations("/etc/ssl/certs/ca-bundle.crt")

    conn = context.wrap_socket(socket.socket(socket.AF_INET),
                               server_hostname="www.python.org")
    conn.connect(("www.python.org", 443))
    cert = conn.getpeercert()
    # {'OCSP': ('http://ocsp.digicert.com',),
    #  'caIssuers': ('http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt',),
    #  'crlDistributionPoints': ('http://crl3.digicert.com/sha2-ev-server-g1.crl',
    #                            'http://crl4.digicert.com/sha2-ev-server-g1.crl'),
    #  'issuer': ((('countryName', 'US'),),
    #             (('organizationName', 'DigiCert Inc'),),
    #             (('organizationalUnitName', 'www.digicert.com'),),
    #             (('commonName', 'DigiCert SHA2 Extended Validation Server CA'),)),
    #  'notAfter': 'Sep  9 12:00:00 2016 GMT',
    #  'notBefore': 'Sep  5 00:00:00 2014 GMT',
    #  'serialNumber': '01BB6F00122B177F36CAB49CEA8B6B26',
    #  'subject': ((('businessCategory', 'Private Organization'),),
    #              (('1.3.6.1.4.1.311.60.2.1.3', 'US'),),
    #              (('1.3.6.1.4.1.311.60.2.1.2', 'Delaware'),),
    #              (('serialNumber', '3359300'),),
    #              (('streetAddress', '16 Allen Rd'),),
    #              (('postalCode', '03894-4801'),),
    #              (('countryName', 'US'),),
    #              (('stateOrProvinceName', 'NH'),),
    #              (('localityName', 'Wolfeboro,'),),
    #              (('organizationName', 'Python Software Foundation'),),
    #              (('commonName', 'www.python.org'),)),
    #  'subjectAltName': (('DNS', 'www.python.org'),
    #                     ('DNS', 'python.org'),
    #                     ('DNS', 'pypi.org'),
    #                     ('DNS', 'docs.python.org'),
    #                     ('DNS', 'testpypi.org'),
    #                     ('DNS', 'bugs.python.org'),
    #                     ('DNS', 'wiki.python.org'),
    #                     ('DNS', 'hg.python.org'),
    #                     ('DNS', 'mail.python.org'),
    #                     ('DNS', 'packaging.python.org'),
    #                     ('DNS', 'pythonhosted.org'),
    #                     ('DNS', 'www.pythonhosted.org'),
    #                     ('DNS', 'test.pythonhosted.org'),
    #                     ('DNS', 'us.pycon.org'),
    #                     ('DNS', 'id.python.org')),
    #  'version': 3}

    conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
    pprint(conn.recv(1024).split(b"\r\n"))
    # [b'HTTP/1.1 200 OK',
    #  b'Date: Sat, 18 Oct 2014 18:27:20 GMT',
    #  b'Server: nginx',
    #  b'Content-Type: text/html; charset=utf-8',
    #  b'X-Frame-Options: SAMEORIGIN',
    #  b'Content-Length: 45679',
    #  b'Accept-Ranges: bytes',
    #  b'Via: 1.1 varnish',
    #  b'Age: 2188',
    #  b'X-Served-By: cache-lcy1134-LCY',
    #  b'X-Cache: HIT',
    #  b'X-Cache-Hits: 11',
    #  b'Vary: Cookie',
    #  b'Strict-Transport-Security: max-age=63072000; includeSubDomains',
    #  b'Connection: close',
    #  b'',
    #  b'']

Server-side operation
=====================
.. code-block:: python

    import socket, ssl


    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="mycertfile", keyfile="mykeyfile")

    bindsocket = socket.socket()
    bindsocket.bind(('myaddr.example.com', 10023))
    bindsocket.listen(5)


    while True:
        newsocket, fromaddr = bindsocket.accept()
        connstream = context.wrap_socket(newsocket, server_side=True)
        try:
            deal_with_client(connstream)
        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()

    def deal_with_client(connstream):
        data = connstream.recv(1024)
        # empty data means the client is finished with us
        while data:
            if not do_something(connstream, data):
                # we'll assume do_something returns False
                # when we're finished with client
                break
            data = connstream.recv(1024)
        # finished with client
