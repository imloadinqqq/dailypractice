import socketserver
import datetime

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("Recieved data from {}:".format(self.client_address[0]))
        print(self.data)

        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    with socketserver.TCPServer((HOST, PORT), MyServer) as server:
        server.serve_forever()
