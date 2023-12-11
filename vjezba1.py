import argparse
import socket
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Python script for working with TCP/UDP and byte order")

    # Optional arguments
    parser.add_argument('-t', action='store_true', help='Use TCP (default)')
    parser.add_argument('-u', action='store_true', help='Use UDP')
    parser.add_argument('-x', action='store_true', help='Use hex (4 hex digits, 2 bytes)')
    parser.add_argument('-H', action='store_true', help='Use host byte order (default)')
    parser.add_argument('-n', action='store_true', help='Use network byte order')

    # Positional arguments
    parser.add_argument('hostname_or_ip', type=str, help='Hostname or IP address')
    parser.add_argument('servicename', type=str, help='Servicename')

    return parser.parse_args()

def set_protocol(args):
    return socket.SOCK_DGRAM if args.u else socket.SOCK_STREAM

def set_byte_order(args):
    return "big" if args.n else "little"

def display_options(args, protocol, byte_order):
    print(f"Hostname/IP: {args.hostname_or_ip}")
    print(f"Servicename: {args.servicename}")
    print(f"Protocol: {'UDP' if args.u else 'TCP'}")
    print(f"Byte Order: {'Network' if args.n else 'Host'}")

    try:
        port_number = socket.getservbyname(args.servicename)
    except socket.error:
        print(f"Error: Invalid servicename")
        sys.exit(1)

    if args.x:
        hex_data = format(port_number, '04X')  
        print(f"Port number: {hex_data}")
    else:
        print(f"Port number: {port_number}")
def get_hostname_from_ip(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return None

def main():
    args = parse_arguments()
    protocol = set_protocol(args)
    byte_order = set_byte_order(args)
    display_options(args, protocol, byte_order)

    if args.hostname_or_ip:
        if args.hostname_or_ip.replace('.', '').isdigit():
            # Ako je input IP, pronadji hostname
            hostname = get_hostname_from_ip(args.hostname_or_ip)
            if hostname:
                print(f"Corresponding hostname: {hostname}")
                args.hostname_or_ip = hostname

    try:
        ip_address = socket.gethostbyname(args.hostname_or_ip)
        canonical_name, _, _ = socket.gethostbyaddr(ip_address)
        print(f"{ip_address} ({canonical_name}) {args.servicename}")
    except socket.herror as e:
        print(f"Error: {e}")

    

    sys.exit(0)  

if __name__ == "__main__":
    main()
