*******************
3rd Party Libraries
*******************


Allegro Ralph
=============
* http://allegro.tech/ralph/
* https://github.com/allegro/ralph

Ralph is full-featured Asset Management, DCIM and CMDB system for data center and back office.

Features:

* keep track of assets purchases and their life cycle
* generate flexible and accurate cost reports
* integrate with change management process using JIRA integration

It is an Open Source project provided on Apache v2.0 License.

Live demo:

* http://ralph-demo.allegro.tech/
* login: ralph
* password: ralph


``Pcapy`` and ``libpcap``
=========================
* Python libpcap module is a low-level binding for libpcap C library.
* http://www.tcpdump.org/manpages/pcap.3pcap.html
* https://www.comparitech.com/net-admin/tcpdump-cheat-sheet/
* https://nmap.org/npcap/
* https://www.secureauth.com/labs/open-source-tools/pcapy
* Pcapy is a Python extension module that interfaces with the libpcap packet capture library.
* Pcapy enables python scripts to capture packets on the network.
* Pcapy is highly effective when used in conjunction with a packet-handling package such as Impacket, which is a collection of Python classes for constructing and dissecting network packets.
* https://github.com/helpsystems/pcapy/tree/master/tests


``Dpkt``
========
* fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
* https://dpkt.readthedocs.io/en/latest/


``Scanpy``
==========


``Twisted``
===========
* An extensible framework for Python programming, with special focus on event-based network programming and multiprotocol integration.
* Twisted includes lots and lots of protocol implementations, meaning that more likely than not there will be an API you can use to talk to some remote system (either client or server in most cases) - be it:

    * HTTP
    * FTP
    * SMTP
    * POP3
    * IMAP4
    * DNS
    * IRC
    * MSN
    * OSCAR
    * XMPP/Jabber
    * telnet
    * SSH
    * SSL
    * NNTP
    * Finger
    * ident
    * lower level protocol-building-protocols like DJB's netstrings
    * simple line-oriented protocols
    * Twisted's custom protocols like Perspective Broker (PB) or Asynchronous Messaging Protocol (AMP).

* none of this functionality is implemented by blocking on the network
* https://twistedmatrix.com/trac/wiki/TwistedProjects

Echo Server
-----------
.. code-block:: python

    from twisted.internet import protocol, reactor, endpoints

    class Echo(protocol.Protocol):
        def dataReceived(self, data):
            self.transport.write(data)

    class EchoFactory(protocol.Factory):
        def buildProtocol(self, addr):
            return Echo()

    endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
    reactor.run()

Web Server
----------
.. code-block:: python

    from twisted.web import server, resource
    from twisted.internet import reactor, endpoints


    class Counter(resource.Resource):
        isLeaf = True
        numberRequests = 0

        def render_GET(self, request):
            self.numberRequests += 1
            request.setHeader(b"content-type", b"text/plain")
            content = f"I am request #{self.numberRequests}\n"
            return content.encode()

    endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(Counter()))
    reactor.run()

Publish/Subscribe
-----------------
.. code-block:: python

    from twisted.internet import reactor, protocol, endpoints
    from twisted.protocols import basic


    class PubProtocol(basic.LineReceiver):
        def __init__(self, factory):
            self.factory = factory

        def connectionMade(self):
            self.factory.clients.add(self)

        def connectionLost(self, reason):
            self.factory.clients.remove(self)

        def lineReceived(self, line):
            for c in self.factory.clients:
                host = self.transport.getHost()
                source = f"<{host}> ".encode()
                c.sendLine(source + line)


    class PubFactory(protocol.Factory):
        def __init__(self):
            self.clients = set()

        def buildProtocol(self, addr):
            return PubProtocol(self)


    endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())
    reactor.run()

IMAP4 Client
------------
.. code-block:: python

    import sys

    from twisted.internet import protocol, defer, endpoints, task
    from twisted.mail import imap4
    from twisted.python import failure


    @defer.inlineCallbacks
    def main(reactor, username=b"myusername", password=b"mypassword",
             strport="tls:example.com:993"):

        endpoint = endpoints.clientFromString(reactor, strport)
        factory = protocol.Factory.forProtocol(imap4.IMAP4Client)

        try:
            client = yield endpoint.connect(factory)
            yield client.login(username, password)
            yield client.select('INBOX')
            info = yield client.fetchEnvelope(imap4.MessageSet(1))
            print('First message subject:', info[1]['ENVELOPE'][1])
        except:
            print("IMAP4 client interaction failed")
            failure.Failure().printTraceback()

    task.react(main, sys.argv[1:])


``Pyro4``
=========
* https://github.com/irmen/Pyro4
* https://pyro4.readthedocs.io/en/stable/
* Pyro means PYthon Remote Objects.
* It is a library that enables you to build applications in which objects can talk to each other over the network, with minimal programming effort.
* You can just use normal Python method calls, with almost every possible parameter and return value type, and Pyro takes care of locating the right object on the right computer to execute the method.
* It is designed to be very easy to use, and to generally stay out of your way.
* But it also provides a set of powerful features that enables you to build distributed applications rapidly and effortlessly.
* Pyro is a pure Python library and runs on many different platforms and Python versions.

