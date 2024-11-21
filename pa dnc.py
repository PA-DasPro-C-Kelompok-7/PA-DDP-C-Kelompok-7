import json
import os
from prettytable import PrettyTable
import pwinput
from datetime import datetime

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk memuat data pengguna dan wisata dari file JSON
def load_data():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {
            'admin': {'password': '123', 'role': 'admin', 'balance': 0, 'transactions': []},
        }
        save_data(users, 'users.json')

    try:
        with open('tourist_spots.json', 'r') as file:
            tourist_spots = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tourist_spots = {
            1: {'name': 'Pantai Kuta', 'price': 30000},
            2: {'name': 'Gunung Bromo', 'price': 50000},
            3: {'name': 'Candi Borobudur', 'price': 20000},
            4: {'name': 'Pulau Komodo', 'price': 80000},
            5: {'name': 'Lake Toba', 'price': 60000},
        }
        save_data(tourist_spots, 'tourist_spots.json')

    return users, tourist_spots

# Fungsi untuk menyimpan data ke file JSON
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Fungsi untuk login
def login(users):
    try:
        clear_screen()
        print("=== Login ===")
        username = input("Username: ")
        password = pwinput.pwinput("password: ","*")

        if username in users and users[username]['password'] == password:
            return username
        else:
            print("Username atau password salah.")
            return None
    except KeyboardInterrupt:
        print("Maaf tidak bisa CTRL+C!")

# Fungsi untuk registrasi user baru
def register(users):
    clear_screen()
    print("=== Registrasi User Baru ===")
    username = input("Username baru: ")
    if username in users:
        print("Username sudah terdaftar. Silakan pilih username lain.")
        return None
    password = pwinput.pwinput("password","*")
    users[username] = {'password': password, 'role': 'user', 'balance': 0, 'transactions': []}
    save_data(users, 'users.json')
    print(f"Registrasi berhasil! Selamat datang, {username}.")
    return username

# Fungsi untuk top-up saldo
def top_up_balance(username, users):
    clear_screen()
    print(f"=== Top-up Saldo untuk {username} ===")
    try:
        amount = int(input("Masukkan jumlah top-up (Rp): "))
        if amount <= 0:
            print("Jumlah top-up harus lebih besar dari 0.")
        elif amount > 5000000:
            print("Jumlah top-up tidak boleh lebih dari Rp 5.000.000.")
        else:
            users[username]['balance'] += amount
            save_data(users, 'users.json')
            print(f"Top-up sebesar Rp {amount} berhasil! Saldo Anda sekarang: Rp {users[username]['balance']}.")
    except ValueError:
        print("Jumlah top-up harus berupa angka.")

# Fungsi untuk menampilkan wisata menggunakan PrettyTable
def show_tours(tourist_spots):
    clear_screen()
    table = PrettyTable()
    table.field_names = ["ID", "Nama Wisata", "Harga (Rp)"]
    
    for id, spot in tourist_spots.items():
        table.add_row([id, spot['name'], spot['price']])

    print(table)

# Fungsi untuk admin menambah, mengubah, dan menghapus wisata
def admin_dashboard(username, users, tourist_spots):
    while True:
        print("\n=== Admin Dashboard ===")
        print("1. Tambah Wisata")
        print("2. Ubah Wisata")
        print("3. Hapus Wisata")
        print("4. Lihat Daftar Wisata")
        print("5. Logout")
        choice = input("Pilih aksi: ")

        if choice == '1':
            add_tour(tourist_spots)
        elif choice == '2':
            update_tour(tourist_spots)
        elif choice == '3':
            delete_tour(tourist_spots)
        elif choice == '4':
            show_tours(tourist_spots)
        elif choice == '5':
            print(f"Admin {username} keluar.")
            break
        else:
            print("Pilihan tidak valid.")
        
        save_data(tourist_spots, 'tourist_spots.json')

# Fungsi untuk menambah wisata baru
def add_tour(tourist_spots):
    print("\n=== Tambah Wisata ===")
    name = input("Nama Wisata: ")
    price = int(input("Harga Wisata: "))

    if tourist_spots:
        new_id = max(int(key) for key in tourist_spots.keys()) + 1
    else:
        new_id = 1
    tourist_spots[new_id] = {'name': name, 'price': price}
    print(f"Wisata '{name}' berhasil ditambahkan.")

# Fungsi untuk mengubah informasi wisata
def update_tour(tourist_spots):
    show_tours(tourist_spots)
    tour_id = int(input("Pilih ID wisata yang ingin diubah: "))
    if tour_id in tourist_spots:
        new_name = input("Nama baru wisata: ")
        new_price = int(input("Harga baru wisata: "))
        tourist_spots[tour_id] = {'name': new_name, 'price': new_price}
        print(f"Wisata dengan ID {tour_id} berhasil diubah.")
    else:
        print("ID wisata tidak ditemukan.")

# Fungsi untuk menghapus wisata
def delete_tour(tourist_spots):
    show_tours(tourist_spots)
    tour_id = int(input("Pilih ID wisata yang ingin dihapus: "))
    if tour_id in tourist_spots:
        del tourist_spots[tour_id]
        print(f"Wisata dengan ID {tour_id} berhasil dihapus.")
    else:
        print("ID wisata tidak ditemukan.")

# Fungsi untuk user memesan tiket
def user_dashboard(username, users, tourist_spots):
    while True:
        print("\n=== User Dashboard ===")
        print("1. Lihat Daftar Wisata")
        print("2. Pesan Tiket")
        print("3. Top-up Saldo")
        print("4. Cek Saldo")
        print("5. Logout")
        choice = input("Pilih aksi: ")

        if choice == '1':
            show_tours(tourist_spots)
        elif choice == '2':
            book_ticket(username, users, tourist_spots)
        elif choice == '3':
            top_up_balance(username, users)
        elif choice == '4':
            check_balance(username, users)
        elif choice == '5':
            print(f"User {username} keluar.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk memesan tiket
def book_ticket(username, users, tourist_spots):
    show_tours(tourist_spots)
    
    # Meminta input ID wisata
    tour_id = input("Pilih ID wisata yang ingin dipesan: ")
    
    # Memeriksa apakah ID wisata valid
    if tour_id.isdigit():
        tour_id = (tour_id)
        if tour_id in tourist_spots:
            price = tourist_spots[tour_id]['price']
            print(f"Anda memilih {tourist_spots[tour_id]['name']} dengan harga Rp {price} per tiket.")
            
            # Meminta input jumlah tiket
            try:
                quantity = int(input("Berapa tiket yang ingin Anda pesan? "))
                if quantity <= 0:
                    print("Jumlah tiket harus lebih dari 0.")
                    return
            except ValueError:
                print("Jumlah tiket harus berupa angka.")
                return

            total_price = price * quantity  # Menghitung total harga untuk tiket yang dibeli
            
            # Memeriksa apakah saldo mencukupi
            if users[username]['balance'] >= total_price:
                users[username]['balance'] -= total_price  # Mengurangi saldo pengguna
                
                # Menyimpan transaksi dan menampilkan invoice
                invoice = generate_invoice(username, tourist_spots[tour_id], total_price, quantity)
                print(invoice)
                
                # Menambahkan transaksi ke daftar transaksi pengguna
                users[username]['transactions'].append({
                    'tour_id': tour_id,
                    'tour_name': tourist_spots[tour_id]['name'],
                    'quantity': quantity,
                    'total_price': total_price,
                    'date': datetime.now().strftime('%Y-%m-%d %H:M:%S')
                })
                
                # Menyimpan perubahan data pengguna ke file
                save_data(users, 'users.json')
            else:
                print("Saldo Anda tidak cukup untuk memesan tiket.")
        else:
            print("ID wisata tidak ditemukan.")
    else:
        print("ID wisata tidak valid.")


# Fungsi untuk mengecek saldo e-money
def check_balance(username, users):
    print(f"Saldo Anda: Rp {users[username]['balance']}")

# Fungsi untuk menghasilkan invoice
def generate_invoice(username, tour, price, quantity):
    invoice = f"""
    ========== INVOICE ==========
    Nama User    : {username}
    Nama Wisata  : {tour['name']}
    Harga per Tiket : Rp {tour['price']}
    Jumlah Tiket   : {quantity}
    Total Harga    : Rp {price}
    Tanggal        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    ============================
    Terima kasih telah melakukan pemesanan!
    """
    return invoice
# Fungsi utama program
def main():
    users, tourist_spots = load_data()

    while True:
        try:
            clear_screen()
            print("=== Sistem Pembelian Tiket Wisata ===")
            print("1. Login")
            print("2. Registrasi User Baru")
            print("3. Keluar")
            choice = input("Pilih aksi: ")

            if choice == '1':
                username = login(users)
                if username:
                    if users[username]['role'] == 'admin':
                        admin_dashboard(username, users, tourist_spots)
                    elif users[username]['role'] == 'user':
                        user_dashboard(username, users, tourist_spots)
            elif choice == '2':
                username = register(users)
                if username:
                    top_up_balance(username, users)
                    user_dashboard(username, users, tourist_spots)
            elif choice == '3':
                print("Terima kasih, program dihentikan.")
                break
            else:
                print("Pilihan tidak valid.")
        except KeyboardInterrupt:
                print("\nMaaf tidak bisa CTRL+C!")
                os.system("pause")
        except EOFError:
            print("\nInput sesuai Menu!")
            os.system("pause")
if __name__ == "__main__":
    main()
