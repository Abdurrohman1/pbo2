#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
class sekolahan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
# Single Inheritance
class guru:
    def mengajar(self):
        print("guru mengajar: ", self.nama, self.umur)
# Single Inheritance
class murid:
    def duduk(self, belajar, mengajar):
        self.nama = belajar
        self.umur = mengajar
# Multiple Inheritance
class walimurid(sekolahan, guru, murid):
    def __init__(self, nama, umur):
        super().__init__(nama, umur)
    def update(self):
        self.mengajar(1, 1)
        self.duduk()