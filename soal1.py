import datetime

def cetak_tanggal(jumlah_hari):
    # memasukkan tanggal hari ini
    hari_ini = datetime.datetime.today()
    
    # Hitung tanggal dari yang di tuju
    tanggal_masa_depan = hari_ini + datetime.timedelta(days=jumlah_hari)
    
    # Format tanggal 
    tanggal_terformat = tanggal_masa_depan.strftime("%A, %d %B %Y")
    
    # Cetak tanggal yang di tuju dengan format
    print("Tanggal {} hari dari sekarang akan menjadi: {}".format(jumlah_hari, tanggal_terformat))

# Memasukkan jumlah ari untuk diproses
jumlah_hari = int(input("Masukkan jumlah hari dari sekarang: "))

# Panggil fungsi untuk mencetak tanggal yang dituju
cetak_tanggal(jumlah_hari)
