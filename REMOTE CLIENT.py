import socket

# Δώσε τη διεύθυνση IP του server (αντικατέστησε με τη σωστή IP του server)
server_ip = '192.168.x.x'  # Αντικατέστησε με την πραγματική IP του server
server_port = 12345

# Δημιουργία socket για τον client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Σύνδεση στον server (χρησιμοποιούμε την IP του server)
client_socket.connect((server_ip, server_port))

print("Συνδέθηκες στον server! Προσπάθησε να μαντέψεις τον αριθμό.")

# Ατελείωτος βρόχος για να μαντέψουμε τον αριθμό
while True:
    # Ο χρήστης εισάγει την εικασία του ή εντολή εξόδου
    message = input("Δώσε έναν αριθμό από το 1 έως το 100 (ή *#0#* για έξοδο): ")
    client_socket.send(message.encode('utf-8'))

    if message == "*#0#*":
        print("Κλείσιμο σύνδεσης.")
        break

    # Λήψη απάντησης από τον server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Απάντηση από τον server: {response}")

    # Έλεγχος αν ο χρήστης βρήκε τον αριθμό
    if response == "Σωστά! Βρήκες τον αριθμό.":
        print("Συγχαρητήρια! Το παιχνίδι τελείωσε.")
        break

client_socket.close()  # Κλείνουμε το socket του client
