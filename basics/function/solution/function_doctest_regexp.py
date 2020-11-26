"""
* Assignment: Function Doctest Regexp
* Solution: discussion
* Complexity: almost impossible
* Lines of code to write: 0 lines
* Estimated time: 5 min

English:
    1. Do not write any code, this is discussion only!
    2. Use data from "Given" section (see below)
    3. Pattern incorrectly classifies `https://foo_bar.example.com/` as invalid
    4. Fix pattern without writing automated tests
    5. Don't break classification of the other cases
    6. Discuss whether this is sane and how tests are helping?

Polish:
    1. Nie pisz żadnego kodu, to jest tylko dyskusja!
    2. Użyj danych z sekcji "Given" (patrz poniżej)
    3. Wyrażenie niepoprawnie klasyfikuje `https://foo_bar.example.com/` jako nieprawidłowy
    4. Popraw wyrażenie bez pisania testów automatycznych
    5. Nie zepsuj klasyfikacji pozostałych przypadków
    6. Przedyskutuj czy ma to sens i czy jak pomagają?

Tests:
    >>> type(PATTERN)
    <class 'str'>
    >>> import re
    >>> url = re.compile(PATTERN)
    # Note that (?:[a-z\x{00a1} will fail in Python
"""

# Author: @diegoperini
# Source: https://mathiasbynens.be/demo/url-regex
PATTERN = r'_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})' \
          r'(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})' \
          r'(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])' \
          r'(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))' \
          r'|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)' \
          r'(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*' \
          r'(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS'

VALID = [
    'http://foo.com/blah_blah',
    'http://foo.com/blah_blah/',
    'http://foo.com/blah_blah_(wikipedia)',
    'http://foo.com/blah_blah_(wikipedia)_(again)',
    'http://www.example.com/wpstyle/?p=364',
    'https://www.example.com/foo/?bar=baz&inga=42&quux',
    'http://✪df.ws/123',
    'http://myusername:mypassword@example.com:8080',
    'http://myusername:mypassword@example.com:8080/',
    'http://myusername@example.com',
    'http://myusername@example.com/',
    'http://myusername@example.com:8080',
    'http://myusername@example.com:8080/',
    'http://myusername:mypassword@example.com',
    'http://myusername:mypassword@example.com/',
    'http://142.42.1.1/',
    'http://142.42.1.1:8080/',
    'http://➡.ws/䨹',
    'http://⌘.ws',
    'http://⌘.ws/',
    'http://foo.com/blah_(wikipedia)#cite-1',
    'http://foo.com/blah_(wikipedia)_blah#cite-1',
    'http://foo.com/unicode_(✪)_in_parens',
    'http://foo.com/(something)?after=parens',
    'http://☺.damowmow.com/',
    'http://code.google.com/events/#&product=browser',
    'http://j.mp',
    'ftp://foo.bar/baz',
    'http://foo.bar/?q=Test%20URL-encoded%20stuff',
    'http://مثال.إختبار',
    'http://例子.测试',
    'http://उदाहरण.परीक्षा',
    'http://-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com',
    'http://1337.net',
    'http://a.b-c.de',
    'http://223.255.255.254',
    'https://foo_bar.example.com/']

INVALID = [
    'http://',
    'http://.',
    'http://..',
    'http://../',
    'http://?',
    'http://??',
    'http://??/',
    'http://#',
    'http://##',
    'http://##/',
    'http://foo.bar?q=Spaces',
    '//',
    '//a',
    '///a',
    '///',
    'http:///a',
    'foo.com',
    'rdar://1234',
    'h://test',
    'http:// shouldfail.com',
    ':// should fail',
    'http://foo.bar/foo(bar)baz quux',
    'ftps://foo.bar/',
    'http://-error-.invalid/',
    'http://a.b--c.de/',
    'http://-a.b.co',
    'http://a.b-.co',
    'http://0.0.0.0',
    'http://10.1.1.0',
    'http://10.1.1.255',
    'http://224.1.1.1',
    'http://1.1.1.1.1',
    'http://123.123.123',
    'http://3628126748',
    'http://.www.foo.bar/',
    'http://www.foo.bar./',
    'http://.www.foo.bar./',
    'http://10.1.1.1',
    'http://10.1.1.254']
