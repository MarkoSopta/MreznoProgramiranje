import socket
import sys

def tcp_client(server_ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (server_ip, port)

    try:
        client_socket.connect(server_address)
        filename = input("Upišite naziv datoteke: ")

        client_socket.sendall(filename.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')

        print("Primljeni podaci:")
        print(data)

    except Exception as e:
        print(f"Greška: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 5 or ('-p' in sys.argv and len(sys.argv) != 4):
        print("Usage: python tcpklijent.py [-p port] server_IP")
        sys.exit(1)

    server_ip = sys.argv[-1]
    port = 1234
    if '-p' in sys.argv:
        port_index = sys.argv.index('-p')
        try:
            port = int(sys.argv[port_index + 1])
        except (IndexError, ValueError):
            print("Neispravna vrijednost za port. Koristi se pretpostavljeni port 1234.")

    tcp_client(server_ip, port)
