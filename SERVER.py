import socket
import random
import threading


# Συνάρτηση που χειρίζεται κάθε client
def handle_client(client_socket, addr):
    print(f"Σύνδεση από {addr}")

    # Ο server επιλέγει έναν τυχαίο αριθμό
    target_number = random.randint(1, 100)
    print(f"Ο σωστός αριθμός είναι: {target_number}")

    # Ξεκινάμε το παιχνίδι
    while True:
        # Λήψη της εικασίας από τον client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Ο client {addr} έστειλε: {data}")

        if data == "*#0#*":
            print(f"Λήφθηκε η εντολή εξόδου από {addr}. Κλείσιμο σύνδεσης.")
            break

        # Μετατροπή της εισόδου του client σε ακέραιο αριθμό
        try:
            guess = int(data)
        except ValueError:
            client_socket.send("Παρακαλώ εισάγετε έναν έγκυρο αριθμό.".encode('utf-8'))
            continue

        # Έλεγχος της εικασίας
        if guess < target_number:
            client_socket.send("Ο αριθμός σου είναι μικρότερος.".encode('utf-8'))
        elif guess > target_number:
            client_socket.send("Ο αριθμός σου είναι μεγαλύτερος.".encode('utf-8'))
        else:
            client_socket.send("Σωστά! Βρήκες τον αριθμό.".encode('utf-8'))
            break

    client_socket.close()  # Κλείνουμε τη σύνδεση με τον client


# Δημιουργία socket για τον server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Σύνδεση στη θύρα 12345
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Ο server ακούει στη θύρα 12345...")

# Περιμένουμε τους clients να συνδεθούν
while True:
    client_socket, addr = server_socket.accept()

    # Δημιουργούμε και ξεκινάμε ένα νέο thread για κάθε client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()

# Κλείσιμο του server socket (αν ο server σταματήσει)
server_socket.close()
