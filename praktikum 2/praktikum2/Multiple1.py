#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
class Siswa:
    def __init__(self, nama, nis):
        self.nama = nama
        self.nis = nis
    def belajar(self):
        print(self.nama, "sedang belajar")

class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")

class SiswaPekerja(Siswa, Pekerja):
    def __init__(self, nama, nis, pekerjaan):
        Siswa.__init__(self, nama, nis)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")
        
Siswa_pekerja = SiswaPekerja("Abdurrohman", "21020", "Programmer")
Siswa_pekerja.belajar() # output: Rahma sedang belajar
Siswa_pekerja.bekerja() # output: Rahma sedang bekerja
Siswa_pekerja.bersosialisasi() # output: Rahma sedang bersosialisasi