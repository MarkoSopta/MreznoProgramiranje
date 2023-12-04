import argparse
import socket
import sys

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        sys.exit(f"Error: Hostname '{hostname}' not found.")

def get_port_number(service_name, proto, order):
    try:
        port = socket.getservbyname(service_name, proto)
        if order == 'n':
            port = socket.htons(port)
        return port
    except (socket.error, OSError):
        sys.exit(f"Error: Service '{service_name}' not found for protocol '{proto}'.")

def print_result(ip_address, port, hex_format):

    if hex_format:
        port = hex(port)
    print(f"IP Address: {ip_address}, Port: {port}")

def main():
    parser = argparse.ArgumentParser(description="Get IP address and port number of a service.")
    parser.add_argument('-t', '--tcp', action='store_true', help="Use TCP (default)")
    parser.add_argument('-u', '--udp', action='store_true', help="Use UDP")
    parser.add_argument('-x', '--hex', action='store_true', help="Print port number in hex")
    parser.add_argument('-n', '--network', action='store_true', help="Print port number in network byte order")
    parser.add_argument('hostname', type=str, help="Hostname to resolve")
    parser.add_argument('servicename', type=str, help="Service name to get port number for")
    args = parser.parse_args()

    if args.tcp and args.udp:
        sys.exit("Error: Options -t and -u cannot be used together.")


    proto = 'tcp' if args.tcp else 'udp'
    order = 'h' if args.host else 'n'

    ip_address = get_ip_address(args.hostname)
    port = get_port_number(args.servicename, proto, order)
    print_result(ip_address, port, args.hex)

if __name__ == "__main__":

    main()
