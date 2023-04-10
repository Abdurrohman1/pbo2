class penulis:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur
        
class Buku:
    def __init__(self,nama,penulis):
        self.nama=nama
        self.penulis=penulis
    def daftar_Penulis(self):
        for penulis in self.penulis:
            print(penulis.nama,penulis.umur)

Penulis1=penulis("abdu",22)
Penulis2=penulis("adi",23)

buku=Buku("python 2",[Penulis1,Penulis2])
buku.daftar_Penulis()          
        