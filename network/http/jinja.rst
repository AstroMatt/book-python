*************************
Templates with ``Jinja2``
*************************


Rationale
=========
* A Jinja template is simply a text file.
* Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.)
* A Jinja template doesn’t need to have a specific extension: ``.html``, ``.xml``, or any other extension is just fine


Syntax
======
.. csv-table:: ``Jinja2`` Syntax
    :header-rows: 1

    "Syntax", "Description"
    "``{% ... %}``", "Statements"
    "``{{ ... }}``", "Expressions to print to the template output"
    "``{# ... #}``", "Comments not included in the template output"
    "``#  ... ##``", "Line Statements"


Example usage
=============
.. code-block:: jinja

    <h1>List of users</h1>

    <table>
        <thead>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Role</th>
            </tr>
        </thead>

        <tbody>

            {% for user in users %}
                <tr>
                    <td>{{ user.firstname }}</td>
                    <td>{{ user.lastname }}</td>

                    {% if user.role == 'admin' %}
                        <td>Administrator</td>
                    {% else %}
                        <td>User</td>
                    {% endif %}
                </tr>
            {% endfor %}

        <tbody>
    </table>


Method Calls
============
.. code-block:: jinja

    {% for page in user.get_created_pages() %}
        ...
    {% endfor %}


Filters
=======
* http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-filters

.. code-block:: jinja

    {{ items|join(', ') }}

.. code-block:: jinja

    {% filter upper %}
        This text becomes uppercase
    {% endfilter %}

Assignment tag
==============
.. code-block:: jinja

    {% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
    {% set key, value = call_something() %}

.. code-block:: jinja

    {% set navigation %}
        <li><a href="/">Index</a>
        <li><a href="/downloads">Downloads</a>
    {% endset %}

.. code-block:: jinja

    {% set reply | wordwrap %}
        You wrote:
        {{ message }}
    {% endset %}

Include
=======
.. code-block:: jinja

    {% include 'header.html' %}
        Body
    {% include 'footer.html' %}

.. code-block:: jinja

    {% for box in boxes %}
        {% include "render_box.html" %}
    {% endfor %}

Conditionals
============
.. code-block:: jinja

    {% if loop.index is divisibleby 3 %}
    {% if loop.index is divisibleby(3) %}

.. code-block:: jinja

    {% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% endfor %}
    </ul>
    {% endif %}

.. code-block:: jinja

    {% if kenny.sick %}
        Kenny is sick.
    {% elif kenny.dead %}
        You killed Kenny!  You bastard!!!
    {% else %}
        Kenny looks okay --- so far
    {% endif %}

.. code-block:: jinja

    {% if user.user_id is odd %}
        {{ user.username|e }} is odd
    {% else %}
        hmm. {{ user.username|e }} looks pretty normal
    {% endif %}


Loops
=====
.. code-block:: jinja

    <ul>
    {% for item in seq %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>

.. code-block:: jinja

    {% for item in items %}
        {{ item }}
    {% else %}
        No items!
    {% endfor %}

.. csv-table:: Loops special variables

    "Variable", "Description"
    "``loop.index``", "The current iteration of the loop. (1 indexed)"
    "``loop.index0``", "The current iteration of the loop. (0 indexed)"
    "``loop.revindex``", "The number of iterations from the end of the loop (1 indexed)"
    "``loop.revindex0``", "The number of iterations from the end of the loop (0 indexed)"
    "``loop.first``", "True if first iteration."
    "``loop.last``", "True if last iteration."
    "``loop.length``", "The number of items in the sequence."
    "``loop.cycle``", "A helper function to cycle between a list of sequences. See the explanation below."
    "``loop.depth``", "Indicates how deep in a recursive loop the rendering currently is. Starts at level 1"
    "``loop.depth0``", "Indicates how deep in a recursive loop the rendering currently is. Starts at level 0"
    "``loop.previtem``", "The item from the previous iteration of the loop. Undefined during the first iteration"
    "``loop.nextitem``", "The item from the following iteration of the loop. Undefined during the last iteration"
    "``loop.change``", "True if previously called with a different value (or not called at all)"

Blocks
======
.. code-block:: jinja

    <title>{% block title %}{% endblock %}</title>
    <h1>{{ self.title() }}</h1>
    {% block body %}{% endblock %}

.. code-block:: jinja

    {% block body %}
        <h3>Table Of Contents</h3>
        ...
        {{ super() }}
    {% endblock %}


Cycle
=====
.. code-block:: jinja

    {% for user in users %}
        <li class="{{ loop.cycle('odd', 'even') }}">{{ user }}</li>
    {% endfor %}


Base Template
=============
.. code-block:: jinja

    <!DOCTYPE html>
    <html lang="en">
    <head>
        {% block head %}
        <link rel="stylesheet" href="style.css" />
        <title>{% block title %}{% endblock %} - My Webpage</title>
        {% endblock %}
    </head>
    <body>
        <div id="content">{% block content %}{% endblock %}</div>
        <div id="footer">
            {% block footer %}
            &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
            {% endblock %}
        </div>
    </body>
    </html>

.. code-block:: jinja

    {% extends "base.html" %}
    {% block title %}Index{% endblock %}
    {% block head %}
        {{ super() }}
        <style type="text/css">
            .important { color: #336699; }
        </style>
    {% endblock %}
    {% block content %}
        <h1>Index</h1>
        <p class="important">
          Welcome to my awesome homepage.
        </p>
    {% endblock %}

Import Macros
=============
.. code-block:: jinja

    {% macro input(name, value='', type='text') -%}
        <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
    {%- endmacro %}

    {%- macro textarea(name, value='', rows=10, cols=40) -%}
        <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols
            }}">{{ value|e }}</textarea>
    {%- endmacro %}

.. code-block:: jinja

    {% import 'forms.html' as forms %}
    <dl>
        <dt>Username</dt>
        <dd>{{ forms.input('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ forms.input('password', type='password') }}</dd>
    </dl>
    <p>{{ forms.textarea('comment') }}</p>

.. code-block:: jinja

    {% from 'forms.html' import input as input_field, textarea %}
    <dl>
        <dt>Username</dt>
        <dd>{{ input_field('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ input_field('password', type='password') }}</dd>
    </dl>
    <p>{{ textarea('comment') }}</p>

i18n Trans
==========
.. code-block:: jinja

    <p>{% trans %}Hello {{ user }}!{% endtrans %}</p>

.. code-block:: jinja

    {% trans count=list|length %}
    There is {{ count }} {{ name }} object.
    {% pluralize %}
    There are {{ count }} {{ name }} objects.
    {% endtrans %}

.. code-block:: jinja

    {{ _('Hello World!') }}
