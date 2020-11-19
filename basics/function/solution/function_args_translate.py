"""
>>> translate('zażółć')
'zazolc'
>>> translate('gęślą')
'gesla'
>>> translate('jaźń')
'jazn'
>>> translate('zażółć gęślą jaźń')
'zazolc gesla jazn'
"""

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}


def translate(text):
    return ''.join(PL.get(x, x) for x in text)
