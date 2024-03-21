# Inisialisasi variabel untuk menyimpan jumlah angka yang dimasukkan
total = 0

# Loop untuk membaca input 
while True:
    # Memasukkan angka
    angka = input("Masukkan angka (atau ketik -1 untuk berhenti): ")
    
    # apa bila memasukkan angka -1 maka akan berhenti
    if angka == '-1':
        break
    
    # Tambahkan angka yang dimasukkan ke total
    total += float(angka)

# Cetak total dengan format desimal dua angka setelah koma
print("{:.2f}".format(total))
