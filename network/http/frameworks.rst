q***************
HTTP Frameworks
***************


``atlassian-python-api``
========================
* https://github.com/atlassian-api/atlassian-python-api

.. code-block:: python

    from atlassian import Confluence
    from atlassian import Jira


    jira = Jira(
        url='http://localhost:8080',
        username='myusername',
        password='mypassword')

    confluence = Confluence(
        url='http://localhost:8090',
        username='myusername',
        password='mypassword')


    JQL = 'project = DEMO AND status NOT IN (Closed, Resolved) ORDER BY issuekey'
    data = jira.jql(JQL)

    status = confluence.create_page(
        space='DEMO',
        title='This is the title',
        body=f'This is the body. You can use <strong>HTML tags</strong>!<div>{data}</div>')

    print(status)


Standard WSGI
=============
* Web Server Gateway Interface


Standard ASGI
=============
* https://asgi.readthedocs.io/en/latest/

ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

Where WSGI provided a standard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous apps, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.


``django``
==========
* https://www.djangoproject.com/
* https://github.com/django/django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

* **Ridiculously fast** - Django was designed to help developers take applications from concept to completion as quickly as possible.
* **Reassuringly secure** - Django takes security seriously and helps developers avoid many common security mistakes.
* **Exceedingly scalable** - Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

.. code-block:: console

    $ pip install django

FastAPI
=======
* https://github.com/tiangolo/fastapi

.. code-block:: console

    $ pip install fastapi uvicorn

.. code-block:: python

    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    def read_root():
        return {"Hello": "World"}


    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "q": q}

.. code-block:: console

    $ uvicorn main:app --reload

*  Automatic API doc generated:

    * OpenAPI (Swagger UI) http://127.0.0.1:8000/docs
    * Redoc http://127.0.0.1:8000/redoc

Examples
--------
.. code-block:: python

    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()


    class Item(BaseModel):
        name: str
        price: float
        is_offer: bool = None


    @app.get("/")
    def read_root():
        return {"Hello": "World"}


    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "q": q}


    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}


``flask``
=========
* http://flask.pocoo.org/

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!

.. code-block:: console

    $ pip install Flask

.. code-block:: console

    $ python hello.py
     * Running on http://localhost:5000/

.. code-block:: console

    $ export FLASK_APP=hello.py
    $ python -m flask run --host=0.0.0.0
     * Running on http://0.0.0.0:5000/

.. literalinclude:: src/http-flask-simple.py
    :name: listing-http-flask-simple
    :language: python
    :caption: Simple usage of Flask

.. literalinclude:: src/http-flask-template.py
    :name: listing-http-flask-template
    :language: python
    :caption: Flask using templates and data from user


``webapp2``
===========
* https://webapp2.readthedocs.io/en/latest/
* https://github.com/GoogleCloudPlatform/webapp2

webapp2 is a lightweight Python web framework compatible with Google App Engine’s webapp.

* **webapp2 is a simple** - it follows the simplicity of webapp, but improves it in some ways: it adds better URI routing and exception handling, a full featured response object and a more flexible dispatching mechanism.
* **webapp2 also offers the package webapp2_extras** - with several optional utilities: sessions, localization, internationalization, domain and subdomain routing, secure cookies and others.
* **webapp2 can also be used outside of Google App Engine**, independently of the App Engine SDK.

.. code-block:: yaml

    application: myapp
    version: 1
    runtime: python27
    api_version: 1
    threadsafe: true

    handlers:
    - url: /.*
      script: main.app

.. code-block:: python

    import webapp2

    class HelloWebapp2(webapp2.RequestHandler):
        def get(self):
            self.response.write('Hello, webapp2!')

    app = webapp2.WSGIApplication([
        ('/', HelloWebapp2),
    ], debug=True)


``tornado``
===========
* http://www.tornadoweb.org/en/stable/
* https://github.com/tornadoweb/tornado

Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

.. code-block:: python

    import tornado.ioloop
    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()
