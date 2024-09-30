# Inisialisasi daftar menu dan harga
menu = {
    "NU GREEN TEA HNY 330": 5000,
    "HYDRO COCO 250ML": 8400,
    "KANZLER BAKSO HOT 55G": 8800,
    "CIMORY UHT CHASEW 250": 7000,
    "CIMORY UHT MARIE 250": 7000,
    "SARI ROTI DORAYAKI COKLAT": 6000,
    "SOSIS BAKAR SAPI": 121000
}

# Inisialisasi keranjang belanja
keranjang = {
    
}

# Fungsi untuk menampilkan daftar menu
def tampilkan_menu():
    print("===== Daftar Menu =====")
    for item, harga in menu.items():
        print(f"{item}: Rp {harga:,.2f}")

# Fungsi untuk menambahkan item ke keranjang
def tambah_ke_keranjang(item):
    if item in menu:
        keranjang.append(item)
        print(f"{item} telah ditambahkan ke keranjang.")
    else:
        print("Item tidak valid. Silakan pilih item yang tersedia.")

# Fungsi untuk menghitung total harga
def hitung_total():
    total = sum([menu[item] for item in keranjang])
    return total

# Fungsi untuk menampilkan struk pembayaran
def tampilkan_struk():
    print("\n--- Struk Pembayaran ---")
    for item in keranjang:
        print(f"{item}: Rp {menu[item]:,.2f}")
    total = hitung_total()
    print(f"Total: Rp {total:,.2f}")
    print("--- Terima kasih! ---")

# Program utama
while True:
    print("\n===== Program Kasir Makanan =====")
    print("1. Tampilkan Menu")
    print("2. Tambahkan Item ke Keranjang")
    print("3. Hitung Total Harga")
    print("4. Tampilkan Struk Pembayaran")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_menu()
    elif pilihan == "2":
        item = input("Masukkan nama item yang ingin ditambahkan: ")
        tambah_ke_keranjang(item)
    elif pilihan == "3":
        total = hitung_total()
        print(f"Total harga dalam keranjang: Rp {total:,.2f}")
    elif pilihan == "4":
        if len(keranjang) > 0:
            tampilkan_struk()
        else:
            print("Keranjang masih kosong. Silakan tambahkan item terlebih dahulu.")
    elif pilihan == "5":
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")
