#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
class Dokter:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nis = nip

    def periksa(self):
        print(self.nama, "sedang memeriksa pasien")

class Spesialis:
    def __init__(self, gelar, tempat):
        self.gelar = gelar
        self.tempat = tempat

    def bekerja(self):
        print(self.tempat, "praktek sedang buka")

class DokterSpesialis(Dokter, Spesialis):
    def __init__(self, nama, nip, gelar, tempat):
        Dokter.__init__(self, nama, nip)
        Spesialis.__init__(self, gelar, tempat)
        
    def seminar(self):
        print(self.nama, self.gelar ,"sedang memberikan seminar")
        
DokterSpesialis_Satu = DokterSpesialis("Abdurrohman", "21020", "(SpKg)", "Cirebon")
DokterSpesialis_Satu.periksa() # output: Rahma sedang belajar
DokterSpesialis_Satu.bekerja() # output: Rahma sedang bekerja
DokterSpesialis_Satu.seminar() # output: Rahma sedang bersosialisasi