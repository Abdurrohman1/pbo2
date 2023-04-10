class Mhs:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur
class kelompok_kkm:
    def __init__(self,nama,mhs):
        self.nama=nama
        self.mhs=mhs
    
    def daftar_mhs(self):
        for mhs in self.mhs:
            print(mhs.nama,mhs.umur)

mhs1=Mhs("abdu",20)
mhs2=Mhs("adu",22)
Kelompok_kkm=kelompok_kkm ("kuat",[mhs1,mhs2])
Kelompok_kkm.daftar_mhs()