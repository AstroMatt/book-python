from multiprocessing.connection import Client
import logging
import pickle

from __init__ import Rectangle


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime).19s] %(levelname)-9s %(name)10s: %(message)s',
    #filename='/_tmp/processes.log'
)

log = logging.getLogger('client')


log.debug('Opening connection')
client = Client(
    address=('localhost', 1337),
    authkey=b'Welcome:)'
)


log.debug('Sending data')
rectangle = Rectangle(5, 10)

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
