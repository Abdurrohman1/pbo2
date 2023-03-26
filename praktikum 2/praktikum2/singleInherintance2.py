#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
class Tumbuhan:
    def __init__(self, namaIlmiah, warna):
        self.namaIlmiah = namaIlmiah
        self.warna = warna

    def fotosintesis(self):
        print(self.namaIlmiah, "Sedang berfotosintesis")

class Bunga(Tumbuhan):
    def __init__(self, namaIlmiah, warna, jenisBunga):
        super().__init__(namaIlmiah, warna)
        self.jenisBunga = jenisBunga

    def mekar(self):
        print("Bunga ", self.jenisBunga, "sedang mekar")


bungaSatu = Bunga("Rosa", "Merah", "Mawar")
bungaSatu.fotosintesis()  # output: Kitty bergerak
bungaSatu.mekar()  # output: Meow!
