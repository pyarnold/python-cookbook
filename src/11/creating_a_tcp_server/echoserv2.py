from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):

    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    print('Echo server running on port 20000')
    serv.serve_forever()
