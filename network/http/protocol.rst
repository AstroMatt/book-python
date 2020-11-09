*************
HTTP Protocol
*************

* Request vs Response
* URI vs URL vs URN
* HTTP vs HTTPS
* HTTP/1.1 vs HTTP/2.0 vs HTTP/3
* Methods
* Statuses
* Headers

URI vs URL vs URN
=================
* URIs identify
* URLs locate;
* Locators are also identifiers, so every URL is also a URI :cite:`URIvsURL`
* There are URIs which are not URLs :cite:`URIvsURL`

Examples

    Roger Pate

This is my name, which is an identifier. It is like a URI, but cannot be a URL, as it tells you nothing about my location or how to contact me. In this case it also happens to identify at least 5 other people in the USA alone.

    4914 West Bay Street, Nassau, Bahamas

This is a locator, which is an identifier for that physical location. It is like both a URL and URI (since all URLs are URIs), and also identifies me indirectly as "resident of..". In this case it uniquely identifies me, but that would change if I get a roommate.

I say "like" because these examples do not follow the required syntax.

HTTP Methods
============
.. csv-table:: HTTP Methods
    :header-rows: 1
    :widths: 15, 25, 60

    "Method", "Function", "Description"
    "GET", "Read", "Requests using GET should only retrieve data and should have no other effect."
    "POST", "Create", "The POST method requests that the server accept the entity enclosed in the request as a new subordinate of the web resource identified by the URI."
    "PUT", "Update/Replace", "The PUT method requests that the enclosed entity be stored under the supplied URI."
    "PATCH", "Partial Update/Modify", "The PATCH method applies partial modifications to a resource."
    "DELETE", "Delete", "The DELETE method deletes the specified resource."
    "HEAD", "Show Headers", "The HEAD method asks for a response identical to that of a GET request, but without the response body."
    "CONNECT", "Connect", "The CONNECT method converts the request connection to a transparent TCP/IP tunnel, usually to facilitate SSL-encrypted communication (HTTPS) through an unencrypted HTTP proxy."
    "OPTIONS", "Show HTTP Methods", "The OPTIONS method returns the HTTP methods that the server supports for the specified URL."
    "TRACE", "Show Trace", "The TRACE method echoes the received request so that a client can see what (if any) changes or additions have been made by intermediate servers."


HTTP Statuses
=============
.. csv-table:: HTTP Status Families
    :header-rows: 1
    :widths: 15, 85

    "Code", "Description"
    "1XX", "Informational"
    "2XX", "Successful"
    "3XX", "Redirection"
    "4XX", "Client Error"
    "5XX", "Server Error"

``1xx`` Informational response
------------------------------
.. csv-table:: HTTP Statuses ``1xx`` Informational response
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "100", "Continue", ""
    "101", "Switching Protocols", ""
    "102", "Processing (WebDAV)", ""
    "103", "Early Hints", ""

``2xx`` Success
---------------
.. csv-table:: HTTP Statuses ``2xx`` Success
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "200", "OK", ""
    "201", "Created", ""
    "202", "Accepted", ""
    "203", "Non-Authoritative Information", ""
    "204", "No Content", ""
    "205", "Reset Content", ""
    "206", "Partial Content", ""
    "207", "Multi-Status (WebDAV)", ""
    "208", "Already Reported (WebDAV)", ""
    "209", "IM Used", ""

``3xx`` Redirection
-------------------
.. csv-table:: HTTP Statuses ``3xx`` Redirection
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "300", "Multiple Choices", ""
    "301", "Moved Permanently", ""
    "302", "Found (Previously 'Moved temporarily')", ""
    "303", "See Other", ""
    "304", "Not Modified", ""
    "305", "Use Proxy", ""
    "306", "Switch Proxy", ""
    "307", "Temporary Redirect", ""
    "308", "Permanent Redirect", ""

``4xx`` Client errors
---------------------
.. csv-table:: HTTP Statuses ``4xx`` Client errors
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "400", "Bad Request", ""
    "401", "Unauthorized", ""
    "402", "Payment Required", ""
    "403", "Forbidden", ""
    "404", "Not Found", ""
    "405", "Method Not Allowed", ""
    "406", "Not Acceptable", ""
    "407", "Proxy Authentication Required", ""
    "408", "Request Timeout", ""
    "409", "Conflict", ""
    "410", "Gone", ""
    "411", "Length Required", ""
    "412", "Precondition Failed", ""
    "413", "Payload Too Large", ""
    "414", "URI Too Long", ""
    "415", "Unsupported Media Type", ""
    "416", "Range Not Satisfiable", ""
    "417", "Expectation Failed", ""
    "418", "I'm a teapot", "This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324"
    "421", "Misdirected Request", ""
    "422", "Unprocessable Entity (WebDAV)", ""
    "423", "Locked (WebDAV)", ""
    "424", "Failed Dependency (WebDAV)", ""
    "426", "Upgrade Required", ""
    "428", "Precondition Required", ""
    "429", "Too Many Requests", ""
    "431", "Request Header Fields Too Large", ""
    "451", "Unavailable For Legal Reasons", ""

``5xx`` Server errors
---------------------
.. csv-table:: HTTP Statuses ``5xx`` Server errors
    :header-rows: 1
    :widths: 15, 25, 60

    "Code", "Status", "Description"
    "500", "Internal Server Error", ""
    "501", "Not Implemented", ""
    "502", "Bad Gateway", ""
    "503", "Service Unavailable", ""
    "504", "Gateway Timeout", ""
    "505", "HTTP Version Not Supported", ""
    "506", "Variant Also Negotiates", ""
    "507", "Insufficient Storage (WebDAV)", ""
    "508", "Loop Detected (WebDAV)", ""
    "510", "Not Extended", ""
    "511", "Network Authentication Required", ""


HTTP Headers
============

HTTP Request Headers
--------------------
.. csv-table:: HTTP Request Headers
    :header-rows: 1
    :widths: 25, 75

    "Header", "Description"
    "Accept", ""
    "Accept-Charset", ""
    "Accept-Encoding", ""
    "Accept-Language", ""
    "Authorization", ""
    "Cache-Control", ""
    "Content-Length", ""
    "Content-Type", ""
    "Cookie", ""
    "Date", ""
    "Host", ""
    "Origin", ""
    "Pragma", ""
    "Referer", ""
    "User-Agent", ""
    "DNT", ""
    "X-Forwarded-For", ""
    "X-Csrf-Token", ""

HTTP Response Headers
---------------------
.. csv-table:: HTTP Response Headers
    :header-rows: 1
    :widths: 25, 75

    "Header", "Description"
    "Access-Control-Allow-Origin", ""
    "Access-Control-Allow-Methods", ""
    "Allow", ""
    "Cache-Control", ""
    "Content-Disposition", ""
    "Content-Encoding", ""
    "Content-Language", ""
    "Content-Length", ""
    "Content-Type", ""
    "Date", ""
    "ETag", ""
    "Expires", ""
    "Last-Modified", ""
    "Location", ""
    "Pragma", ""
    "Server", ""
    "Set-Cookie", ""
    "WWW-Authenticate", ""
    "X-Frame-Options", ""
    "Refresh", ""
    "Status", ""


MIME types
==========

General structure
-----------------
.. code-block:: text

    type/subtype

.. csv-table:: Types
    :header-rows: 1

    "MIME type", "Description"
    "text", "Represents any document that contains text and is theoretically human readable"
    "image", "Represents any kind of images. Videos are not included, though animated images (like animated gif) are described with an image type"
    "audio", "Represents any kind of audio files"
    "video", "Represents any kind of video files"
    "application", "Represents any kind of binary data"

Text Types
----------
.. csv-table:: Text Types
    :header-rows: 1

    "MIME type", "Description"
    "text/plain", ""
    "text/html", ""
    "text/css", ""

Application Types
-----------------
.. csv-table:: Application Types
    :header-rows: 1

    "MIME type", "Description"
    "application/json", ""
    "application/javascript", ""
    "application/ecmascript", ""
    "application/octet-stream", "As it really means unknown binary"
    "application/pkcs12", ""
    "application/vnd.mspowerpoint", ""
    "application/xhtml+xml", ""
    "application/xml", ""
    "application/pdf", ""
    "application/ogg", "An audio or video file using the OGG container format. Theora is the usual video codec used within it; Vorbis is the usual audio codec"
    "application/*", ""

Multipart Types
---------------
.. csv-table:: Multipart Types
    :header-rows: 1

    "MIME type", "Description"
    "multipart/form-data", ""
    "multipart/byteranges", ""

Image Types
-----------
.. csv-table:: Image types
    :header-rows: 1

    "MIME type", "Description"
    "image/gif", "GIF images (lossless compression, superseded by PNG)"
    "image/jpeg", "JPEG images"
    "image/png", "PNG images"
    "image/svg+xml", "SVG images (vector images)"
    "image/x-icon", "Windows icons"
    "image/bmp", ""
    "image/webp", ""
    "image/vnd.microsoft.icon", ""

Audio Types
-----------
.. csv-table:: Audio Types
    :header-rows: 1

    "MIME type", "Description"
    "audio/wave", ""
    "audio/wav", ""
    "audio/x-wav", ""
    "audio/x-pn-wav", "An audio file in the WAVE container format. The PCM audio codec (WAVE codec '1') is often supported, but other codecs have more limited support (if any)"
    "audio/webm", "An audio file in the WebM container format. Vorbis and Opus are the most common audio codecs"
    "audio/ogg", "An audio file in the OGG container format. Vorbis is the most common audio codec used in such a container"
    "audio/midi", ""
    "audio/mpeg", ""
    "audio/*", ""

Video Types
-----------
.. csv-table:: Video Types
    :header-rows: 1

    "MIME type", "Description"
    "video/mp4", ""
    "video/webm", ""
    "video/ogg", ""
    "video/webm", "A video file, possibly with audio, in the WebM container format. VP8 and VP9 are the most common video codecs used within it; Vorbis and Opus the most common audio codecs"
    "video/ogg", "A video file, possibly with audio, in the OGG container format. Theora is the usual video codec used within it; Vorbis is the usual audio codec"


API Versioning
==============

Good Engineering Practices
--------------------------
* Always version API
* Have stable API!
* Do not use plural in resources
* Use HTTP Statuses
* Use HTTP Methods

How to version API?
-------------------
* Semantic versioning
* Django versioning
* API deprecation policy

.. csv-table:: How to version API?
    :header-rows: 1

    "Example", "Description"
    "``/api/v2/user/10``", "API version as a part of URL"
    "``X-API-VERSION: 2``", "Version as a custom header with ``X-...`` prefix"
    "``/user/10?api=v2``", "Version as a parameter to URL"
    "``Accept: application/vnd.api.v2``", "API version as a custom vendor prefix for ``Accept`` header"
    "``Accept: application/vnd.api.v2;q=0.9,application/vnd.api.v1;q=0.8``", "API version negotiation with weights using ``Accept`` header"
    "api-v2.myhost.com", "Subdomain"
