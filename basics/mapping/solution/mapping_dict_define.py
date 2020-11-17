"""
>>> assert type(result) is dict
>>> assert 'firstname' in result
>>> assert 'lastname' in result
>>> assert 'missions' in result
>>> assert result['firstname'] == 'Jan'
>>> assert result['lastname'] == 'Twardowski'
>>> assert 'Artemis' in result['missions']
>>> assert 'Ares' in result['missions']
>>> assert type(result['missions']) is list
"""

result = {
    'firstname': 'Jan',
    'lastname': 'Twardowski',
    'missions': ['Artemis', 'Ares'],
}
