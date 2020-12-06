from dataclasses import dataclass
from multiprocessing.connection import Client
import logging
import pickle

logging.basicConfig(
    level=logging.DEBUG,
    #filename='/_tmp/processes.log',
    format='[%(asctime).19s] %(levelname)-9s %(name)10s: %(message)s')

log = logging.getLogger('client')


@dataclass
class Point:
    x: int
    y: int


log.debug('Opening connection')
client = Client(
    address=('localhost', 1337),
    authkey=b'Welcome:)'
)


log.debug('Sending data')
rectangle = Point(x=1, y=2)

pickled = pickle.dumps(rectangle, protocol=pickle.HIGHEST_PROTOCOL)

data = ['ehlo', 10, 10.6, None, True, {'asd': 10}, [{1, 2, 3}], rectangle, pickled]

for element in data:
    client.send(element)


log.debug('Closing connection')
client.send('close')
client.close()


## Stworzenie Listenera
# stworzenie listenera
# akceptacja połączeń przychodzących
# pętla
#     przyjecie wiadomości
#     if wiadomość == close: zamkniecie połączenia, wyjście z pętli
#     else: wyświetl treść
# zamknięcie listenera
