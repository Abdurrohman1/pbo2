
class Mahasiswa:
     def __init__(self, nama, nim):
         self.nama = nama
         self.nim = nim
     def info(self):
         print(f"Nama: {self.nama}\nNIM: {self.nim}")
mahasiswaB = Mahasiswa("Abdu", "123456789")
mahasiswaB.info()