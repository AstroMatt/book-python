from socketserver import BaseRequestHandler, TCPServer


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1337


class RequestHandler(BaseRequestHandler):
    def handle(self):
        received = self.request.recv(1024).decode()
        print(f'From: {self.client_address}/TCP, received: "{received}"')

        response = 'Thanks'
        self.request.sendall(response.encode())


with TCPServer((SERVER_HOST, SERVER_PORT), RequestHandler) as server:
    print(f'Accepting connections on {SERVER_HOST}:{SERVER_PORT}/TCP...')
    print(f'To stop the server use `Ctrl-C`\n')
    server.serve_forever()
