import argparse
import socket


def parse_arguments():
    parser = argparse.ArgumentParser(description='TCP klijent')
    parser.add_argument('server_ip', help='IP adresa ili naziv poslužitelja')
    parser.add_argument('-p', '--port', type=int, default=1234, help='Broj porta poslužitelja')
    return parser.parse_args()


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
    args = parse_arguments()
    tcp_client(args.server_ip, args.port)
