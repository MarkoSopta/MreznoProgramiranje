import socket
import sys

def udp_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', port))

    print(f"Server listening on port {port}")

    data, client_address = server_socket.recvfrom(256)
    data = data.decode('utf-8').rstrip('\n')

    num_characters = len(data)
    num_a = data.count('a')

    result = bytes([num_characters, num_a])
    server_socket.sendto(result, client_address)

    print(f"Received: {data}")
    print(f"Sent: {result}")

if __name__ == "__main__":
    port = 1234
    if len(sys.argv) == 3 and sys.argv[1] == '-p':
        port = int(sys.argv[2])

    try:
        udp_server(port)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
