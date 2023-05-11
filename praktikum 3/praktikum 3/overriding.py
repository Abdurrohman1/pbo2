class Pekerjaan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        
    def deskripsi(self):
        return f"Pekerjaan {self.nama} dengan gaji {self.gaji}"
        
class Guru(Pekerjaan):
    def deskripsi(self):
        return f"Guru mengajar di sekolah dengan gaji {self.gaji}"
        
class Dokter(Pekerjaan):
    def deskripsi(self):
        return f"Dokter bekerja di rumah sakit dengan gaji {self.gaji}"
        
class Programmer(Pekerjaan):
    def deskripsi(self):
        return f"Programmer membuat aplikasi dengan gaji {self.gaji}"


guru = Guru("Guru", 5000000)
dokter = Dokter("Dokter", 10000000)
programmer = Programmer("Programmer", 8000000)


print(guru.deskripsi())  
print(dokter.deskripsi())
print(programmer.deskripsi())  