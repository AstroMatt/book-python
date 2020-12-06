import logging
import os
from dataclasses import dataclass
from datetime import timedelta, datetime
import requests


logging.basicConfig(
    level=logging.INFO,
    format='"%(asctime).19s", "%(levelname)s", "%(message)s"'
)
log = logging.getLogger(__name__)


class Cache:
    def __init__(self, expiration: timedelta = timedelta(days=1), location: str = '') -> None:
        self.location = location
        self.expiration = expiration

    def get(self, key: str) -> str:
        raise NotImplementedError

    def set(self, key: str, value: str) -> None:
        raise NotImplementedError

    def is_valid(self, key: str) -> bool:
        raise NotImplementedError


class CacheFilesystem(Cache):
    def __init__(self, location: str = 'tmp', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.location = location

        if not os.path.isdir(self.location):
            if os.path.isfile(self.location):
                os.remove(self.location)
            os.mkdir(self.location)

    def _get_cache_path(self, key: str) -> str:
        filename = key.replace('/', '-').replace(':', '').replace('--', '-')
        return os.path.join(self.location, filename)

    def get(self, key: str) -> str:
        filename = self._get_cache_path(key)

        if not os.path.isfile(filename):
            raise FileNotFoundError

        with open(filename, mode='r', encoding='utf-8') as file:
            return file.read()

    def set(self, key: str, value: str) -> None:
        filename = self._get_cache_path(key)

        if value is None:
            raise ValueError('Value cannot be None')

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(value)

    def is_valid(self, key):
        filename = self._get_cache_path(key)

        if not os.path.isfile(filename):
            return False

        last_modification = os.path.getmtime(filename)
        last_modification = datetime.fromtimestamp(last_modification)
        now = datetime.now()

        if (now - last_modification) > self.expiration:
            return False
        else:
            return True


@dataclass
class HTTPGateway:
    _cache: Cache

    def get(self, url):

        if not self._cache.is_valid(url):
            log.info('Downloading...')
            html = requests.get(url).text
            self._cache.set(url, html)
            log.info('Done.')

        return self._cache.get(url)


if __name__ == '__main__':
    cache = CacheFilesystem(expiration=timedelta(seconds=2), location='tmp')
    # cache = CacheDatabase(expiration=timedelta(minutes=2), location='database.sqlite')
    # cache = CacheMemory(expiration=timedelta(minutes=2))

    http = HTTPGateway(cache)

    html = http.get('http://python.astrotech.io')
    print(html)
