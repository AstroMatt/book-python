*************
SOAP and WSDL
*************


WSDL
====
.. glossary::

    WSDL
    Web Services Description Language
        is an XML-based interface description language that is used for describing the functionality offered by a web service. The acronym is also used for any specific WSDL description of a web service (also referred to as a WSDL file), which provides a machine-readable description of how the service can be called, what parameters it expects, and what data structures it returns. Therefore, its purpose is roughly similar to that of a type signature in a programming language :cite:`DefinitionWSDL`.

    WADL
    Web Application Description Language
        Machine-readable XML description of HTTP-based web services. WADL models the resources provided by a service and the relationships between them.[1] WADL is intended to simplify the reuse of web services that are based on the existing HTTP architecture of the Web. It is platform and language independent and aims to promote reuse of applications beyond the basic use in a web browser.

        WADL was submitted to the World Wide Web Consortium by Sun Microsystems on 31 August 2009, but the consortium has no current plans to standardize it. WADL is the REST equivalent of SOAP's Web Services Description Language (WSDL), which can also be used to describe REST web services.

Main Structure
--------------

.. code-block:: xml

    <definitions>

    <types>
      data type definitions........
    </types>

    <message>
      definition of the data being communicated....
    </message>

    <portType>
      set of operations......
    </portType>

    <binding>
      protocol and data format specification....
    </binding>

    </definitions>


Examples
--------
* In this example the <portType> element defines "glossaryTerms" as the name of a port, and "getTerm" as the name of an operation.
* The "getTerm" operation has an input message called "getTermRequest" and an output message called "getTermResponse".
* The <message> elements define the parts of each message and the associated data types.

.. code-block:: xml

    <message name="getTermRequest">
      <part name="term" type="xs:string"/>
    </message>

    <message name="getTermResponse">
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="getTerm">
        <input message="getTermRequest"/>
        <output message="getTermResponse"/>
      </operation>
    </portType>

The <portType> Element
^^^^^^^^^^^^^^^^^^^^^^
* The <portType> element defines a web service, the operations that can be performed, and the messages that are involved.
* The request-response type is the most common operation type, but WSDL defines four types:

.. csv-table::
    :header-rows: 1

    "Type", "Definition"
    "One-way", "The operation can receive a message but will not return a response"
    "Request-response", "The operation can receive a request and will return a response"
    "Solicit-response", "The operation can send a request and will wait for a response"
    "Notification", "The operation can send a message but will not wait for a response"


WSDL One-Way Operation
----------------------
.. code-block:: xml

    <message name="newTermValues">
      <part name="term" type="xs:string"/>
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="setTerm">
        <input name="newTerm" message="newTermValues"/>
      </operation>
    </portType >


WSDL Request-Response Operation
-------------------------------
.. code-block:: xml

    <message name="getTermRequest">
      <part name="term" type="xs:string"/>
    </message>

    <message name="getTermResponse">
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="getTerm">
        <input message="getTermRequest"/>
        <output message="getTermResponse"/>
      </operation>
    </portType>


WSDL Binding to SOAP
--------------------
.. code-block:: xml

    <message name="getTermRequest">
      <part name="term" type="xs:string"/>
    </message>

    <message name="getTermResponse">
      <part name="value" type="xs:string"/>
    </message>

    <portType name="glossaryTerms">
      <operation name="getTerm">
        <input message="getTermRequest"/>
        <output message="getTermResponse"/>
      </operation>
    </portType>

    <binding type="glossaryTerms" name="b1">
       <soap:binding style="document"
       transport="http://schemas.xmlsoap.org/soap/http" />
       <operation>
         <soap:operation soapAction="http://example.com/getTerm"/>
         <input><soap:body use="literal"/></input>
         <output><soap:body use="literal"/></output>
      </operation>
    </binding>

Example WSDL file
-----------------
.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <description xmlns="http://www.w3.org/ns/wsdl"
                 xmlns:tns="http://www.tmsws.com/wsdl20sample"
                 xmlns:whttp="http://schemas.xmlsoap.org/wsdl/http/"
                 xmlns:wsoap="http://schemas.xmlsoap.org/wsdl/soap/"
                 targetNamespace="http://www.tmsws.com/wsdl20sample">

    <documentation>
        This is a sample WSDL 2.0 document.
    </documentation>

    <!-- Abstract type -->
       <types>
          <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
                    xmlns="http://www.tmsws.com/wsdl20sample"
                    targetNamespace="http://www.example.com/wsdl20sample">

             <xs:element name="request"> ... </xs:element>
             <xs:element name="response"> ... </xs:element>
          </xs:schema>
       </types>

    <!-- Abstract interfaces -->
       <interface name="Interface1">
          <fault name="Error1" element="tns:response"/>
          <operation name="Get" pattern="http://www.w3.org/ns/wsdl/in-out">
             <input messageLabel="In" element="tns:request"/>
             <output messageLabel="Out" element="tns:response"/>
          </operation>
       </interface>

    <!-- Concrete Binding Over HTTP -->
       <binding name="HttpBinding" interface="tns:Interface1"
                type="http://www.w3.org/ns/wsdl/http">
          <operation ref="tns:Get" whttp:method="GET"/>
       </binding>

    <!-- Concrete Binding with SOAP-->
       <binding name="SoapBinding" interface="tns:Interface1"
                type="http://www.w3.org/ns/wsdl/soap"
                wsoap:protocol="http://www.w3.org/2003/05/soap/bindings/HTTP/"
                wsoap:mepDefault="http://www.w3.org/2003/05/soap/mep/request-response">
          <operation ref="tns:Get" />
       </binding>

    <!-- Web Service offering endpoints for both bindings-->
       <service name="Service1" interface="tns:Interface1">
          <endpoint name="HttpEndpoint"
                    binding="tns:HttpBinding"
                    address="http://www.example.com/rest/"/>
          <endpoint name="SoapEndpoint"
                    binding="tns:SoapBinding"
                    address="http://www.example.com/soap/"/>
       </service>
    </description>

Example WADL
------------
* :cite:`DefinitionWADL`

.. code-block:: xml

     <application xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://wadl.dev.java.net/2009/02 wadl.xsd"
      xmlns:tns="urn:yahoo:yn" xmlns:yn="urn:yahoo:yn" xmlns:ya="urn:yahoo:api"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns="http://wadl.dev.java.net/2009/02">
       <grammars>
         <include href="NewsSearchResponse.xsd"/>
         <include href="Error.xsd"/>
       </grammars>

       <resources base="http://api.search.yahoo.com/NewsSearchService/V1/">
         <resource path="newsSearch">
           <method name="GET" id="search">
             <request>
               <param name="appid" type="xsd:string" style="query" required="true"/>
               <param name="query" type="xsd:string" style="query" required="true"/>
               <param name="type" style="query" default="all">
                 <option value="all"/>
                 <option value="any"/>
                 <option value="phrase"/>
               </param>
               <param name="results" style="query" type="xsd:int" default="10"/>
               <param name="start" style="query" type="xsd:int" default="1"/>
               <param name="sort" style="query" default="rank">
                 <option value="rank"/>
                 <option value="date"/>
               </param>
               <param name="language" style="query" type="xsd:string"/>
             </request>
             <response status="200">
               <representation mediaType="application/xml" element="yn:ResultSet"/>
             </response>
             <response status="400">
               <representation mediaType="application/xml" element="ya:Error"/>
             </response>
           </method>
         </resource>
       </resources>
     </application>


``suds``
========
.. code-block:: python

    from suds.client import Client

    client = Client("http://example.com/foo.wsdl")
    client.service.someMethod(someParameter)

.. code-block:: python

    from suds.client import Client

    # The service URL
    soap_url = 'http://myapp.example.com/path/to/soap'

    # The WSDL URL, we wont' use this but just illustrating for example. This
    # would be the file you download to your system and save as wsdl_file
    wsdl_url = 'http://myapp.example.com/path/to/soap?wsdl'

    # The full path to the downloaded WSDL file on your local system
    wsdl_file = '/path/to/myapp.wsdl'
    wsdl_url = 'file://' + wsdl_file # Override original wsdl_url

    client = Client(url=wsdl_url, location=soap_url)


``zeep``
========
* maintained

.. code-block:: python

    from zeep import Client

    client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
    result = client.service.ConvertSpeed(100, 'kilometersPerHour', 'milesPerHour')

    assert result == 62.137

.. code-block:: python

    import zeep

    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    print(client.service.Method1('Zeep', 'is cool'))
