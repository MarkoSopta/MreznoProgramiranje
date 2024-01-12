import socket
import sys

def udp_client(server_ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data = input("Unesite redak podataka: ")
    client_socket.sendto(data.encode('utf-8'), (server_ip, port))

    result, _ = client_socket.recvfrom(2)
    result = list(result)

    num_characters = result[0]
    num_a = result[1]

    print(f"{num_characters} znakova")
    print(f"{num_a} slova a")

if __name__ == "__main__":
    server_ip = None
    port = 1234

    if len(sys.argv) == 3 and sys.argv[1] == '-p':
        port = int(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == '-p':
        port = int(sys.argv[2])
        server_ip = sys.argv[3]
    elif len(sys.argv) == 2:
        server_ip = sys.argv[1]
    else:
        print("Usage: udpklijent.py [-p port] server_IP", file=sys.stderr)
        sys.exit(1)

    try:
        udp_client(server_ip, port)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
