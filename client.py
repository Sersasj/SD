# -*- coding: utf-8 -*-


import Pyro4

def main():
    Pyro4.config.SERIALIZER = "pickle"
    Pyro4.config.SERIALIZERS_ACCEPTED.add("pickle")

    server_names = ["1", "2"]
    server_ports = [9090, 9091]
    servers = [Pyro4.Proxy(f"PYRO:{name}@localhost:{port}") for name, port in zip(server_names, server_ports)]
    while True:
        request = input("Insira uma mensagem: ")

        for server in servers:
            try:
                response = server.process_request(request)
                print(f"Resposta: {response}")
                break
            except Pyro4.errors.CommunicationError:
                print(f"Servidor não disponível. Tentando outro")

if __name__ == "__main__":
    main()