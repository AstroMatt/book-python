#!/bin/sh

DIR='/Users/matt/Developer/book-python'

echo -n > /tmp/pybook.urls

egrep -h --only-matching --include="*.py" -R -e "https://raw(.*)" $DIR >> /tmp/pybook.urls
egrep -h --only-matching --include="*.rst" -R -e "https://raw(.*)" $DIR >> /tmp/pybook.urls

egrep -h --only-matching --include="*.py" -R -e "https://python.astrotech.io/_static/(.*)" $DIR >> /tmp/pybook.urls
egrep -h --only-matching --include="*.rst" -R -e "https://python.astrotech.io/_static/(.*)" $DIR >> /tmp/pybook.urls

cat /tmp/pybook.urls \
  |sort \
  |uniq \
  |sed -e "s/'//" \
  |sed -e 's/"//' \
  |sed -e 's/)//' \
  |xargs curl -o /dev/null --silent --head --write-out '%{url_effective}: %{http_code}\n' \
  |grep https \
  |grep -v 200

rm /tmp/pybook.urls
