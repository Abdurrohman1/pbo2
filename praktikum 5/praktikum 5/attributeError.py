class Guru:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

Guru1 = Guru("Renjun", 22)

try:
    print(Guru1.grup)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")