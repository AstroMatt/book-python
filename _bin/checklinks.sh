#!/bin/sh

egrep -h --only-matching --include="*.py" -R -e "https://raw[^']+" . > /tmp/pybook-py.urls
egrep -h --only-matching --include="*.rst" -R -e "https://raw[^']+" . > /tmp/pybook-rst.urls
cat /tmp/pybook-py.urls /tmp/pybook-rst.urls |sort |uniq |sed -e 's/")//' > /tmp/pybook.urls
cat /tmp/pybook.urls |xargs curl -o /dev/null --silent --head --write-out '%{url_effective}: %{http_code}\n' |grep https |grep -v 200
