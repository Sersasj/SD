# -*- coding: utf-8 -*-


import Pyro4
@Pyro4.expose
class Server():
    def __init__(self, server_name):
        self.server_name = server_name

    def process_request(self, request):
        return f"Servidor {self.server_name}: {request}"

def main():
    Pyro4.config.SERIALIZER = "pickle"
    Pyro4.config.SERIALIZERS_ACCEPTED.add("pickle")

    server = Server("2")

    daemon = Pyro4.Daemon()
    daemon = Pyro4.Daemon(port=9091) 
    uri = daemon.register(server, objectId="2")
    
    print(f"Servidor 2 escutando na porta {uri}")
    daemon.requestLoop()

if __name__ == "__main__":
    main()