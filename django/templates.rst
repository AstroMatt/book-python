*********
Templates
*********

* dir convention

* staticfiles
* url reversing
* simpletags
* templatetags
* using filters
* importing modules
* localizing
* extending templates
* importing templates

.. code-block:: html

    {% load i18n %}


    <table>
        <tr>
            <th>{% trans 'No.' %}</th>
            <th>{% trans 'First Name' %}</th>
            <th>{% trans 'Last Name' %}</th>
            <th>{% trans 'Date of Birth' %}</th>
            <th>{% trans 'Age' %}</th>
        </tr>

    {% for contact in contacts %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>{{ contact.firstname }}</td>
            <td><a href="{% url 'contact:details' contact.id %}">{{ contact.lastname }}</a></td>
            <td>{{ contact.date_of_birth|date:'Y-m-d' }}</td>
            <td>{{ contact.get_age|default_if_none:'n/a' }}</td>
        </tr>
    {% empty %}
        <h2>{% trans 'No contacts' %}</h2>
    {% endfor %}
    </table>
