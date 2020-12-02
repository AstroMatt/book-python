import json
from threading import Timer
import socket
from dataclasses import dataclass


@dataclass
class Heartbeat:
    host: str = '127.0.0.1'
    port: int = 1337
    frequency: float = 1.0

    def start(self):
        Timer(self.frequency, self.ping).start()

    def ping(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            data = json.dumps({
                'host': self.host,
                'port': '%27'
            })
            sock.sendto(data.encode(), (self.host, self.port))

        self.start()


if __name__ == '__main__':
    Heartbeat(frequency=1.0).start()
