class BMI:
    def __init__(self, berat_kg, tinggi_m):
        self.berat_kg = berat_kg
        self.tinggi_m = tinggi_m
    
    @property
    def berat(self):
        return self.berat_kg
    
    @property
    def tinggi(self):
        return self.tinggi_m
    
    def hitung_bmi(self):
        if self.tinggi_m == 0:
            return "Error: Tinggi tidak boleh nol."
        return self.berat_kg / (self.tinggi_m ** 2)

# Contoh penggunaan:
berat = 70  # dalam kilogram
tinggi = 1.75  # dalam meter

# Membuat sebuah instance dari kelas
orang = BMI(berat, tinggi)

# Mendapatkan properti berat dan tinggi
print("Berat:", orang.berat, "kg")
print("Tinggi:", orang.tinggi, "m")

# Menghitung BMI
bmi = orang.hitung_bmi()
print("BMI:", bmi)
