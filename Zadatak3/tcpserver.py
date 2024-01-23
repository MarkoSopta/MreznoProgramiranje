import socket
import sys

def tcp_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', port)

    try:
        server_socket.bind(server_address)
        server_socket.listen(1)

        print(f"Poslužitelj čeka na portu {port}...")
        while True:
            connection, client_address = server_socket.accept()
            try:
                print("Klijent povezan:", client_address)
                filename = connection.recv().decode('utf-8')
                if filename == 'Kraj':
                    print("Primljen signal za završetak. Završavam s radom.")
                    break

                try:
                    with open(filename, 'r') as file:
                        content = file.read()
                        connection.sendall(content.encode('utf-8'))
                        print("Datoteka poslana klijentu.")
                except FileNotFoundError:
                    print(f"Datoteka '{filename}' ne postoji. Slanje poruke o grešci.")
                    connection.sendall("Datoteka ne postoji.".encode('utf-8'))
                except Exception as e:
                    print(f"Greška prilikom obrade klijentskog zahtjeva: {e}")

            finally:
                connection.close()

    except Exception as e:
        print(f"Greška: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    port = 1234
    if '-p' in sys.argv:
        port_index = sys.argv.index('-p')
        try:
            port = int(sys.argv[port_index + 1])
        except (IndexError, ValueError):
            print("Neispravna vrijednost za port. Koristi se pretpostavljeni port 1234.")

    tcp_server(port)
