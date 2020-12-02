from socketserver import BaseRequestHandler, UDPServer


HOST = '127.0.0.1'
PORT = 1337


class RequestHandler(BaseRequestHandler):
    def handle(self):
        received = self.request.recv(1024).decode()
        print(f'From: {self.client_address}/TCP, received: "{received}"')

        response = 'Thanks'
        self.request.sendto(response.encode(), self.client_address)


with UDPServer((HOST, PORT), RequestHandler) as server:
    print(f'Accepting connections on {HOST}:{PORT}/UDP...')
    print(f'To stop the server use `Ctrl-C`\n')
    server.serve_forever()
