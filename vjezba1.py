import argparse
import socket
import sys

def main():
    # Parsiranje argumenata
    parser = argparse.ArgumentParser(description="Dohvati IP adresu, CNAME i broj porta usluge")
    parser.add_argument("hostname", help="Ime računala")
    parser.add_argument("servicename", help="Naziv usluge")
    parser.add_argument("-u", "--udp", action="store_true", help="Koristi UDP protokol (TCP je pretpostavljen)")
    parser.add_argument("-x", "--hex", action="store_true", help="Ispisi broj porta u heksadecimalnom obliku")
    parser.add_argument("-n", "--network", action="store_true", help="Prikaži broj porta u network byte redoslijedu")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        print("Uporaba:")
        print("  getaddrinfo.py [-t|-u] [-x] [-h|-n] hostname servicename")
        print("Opcije:")
        print("  -t, --tcp         Koristi TCP protokol (TCP je pretpostavljen)")
        print("  -u, --udp         Koristi UDP protokol")
        print("  -x, --hex         Ispisi broj porta u heksadecimalnom obliku")
        print("  -n, --network     Prikaži broj porta u network byte redoslijedu")
        sys.exit()

    # Dohvati informacije o servisu
    try:
        for info in socket.getaddrinfo(args.hostname, args.servicename, protocol=protocol):
            address, _, _, _, port = info
            break
    except socket.gaierror as e:
        print(f"Greška: {e}", file=sys.stderr)
        sys.exit(1)
     # Rukovanje greskama
    if args.udp:
        if args.tcp:
            print("Greška: Mogu se koristiti samo jedna od opcija -t i -u", file=sys.stderr)
            sys.exit(1)
        if args.hex and args.network:
            print("Greška: Mogu se koristiti samo jedna od opcija -x i -n", file=sys.stderr)
            sys.exit(1)
    if info is None:
        print("Greška: Ne postoji adresa za navedene parametre", file=sys.stderr)
        sys.exit(1)

    # Transportni protokol
    protocol = socket.AF_INET if not args.udp else socket.AF_INET6

    # Ispisi IP adresu i CNAME
    if address:
        print(f"{address[0]} {socket.gethostbyaddr(address)[0]}", end=" ")

    # Formatiranje porta
    port_format = "x" if args.hex else "d"
    byte_order = "!" if args.network else ""

    # Ispisi broj porta
    print(f"{port:{port_format}{byte_order}}")

if __name__ == "__main__":
    main()
