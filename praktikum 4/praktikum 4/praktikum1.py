class peneliti:
    def __init__(self,nama,umur):
        self.nama=nama 
        self.umur=umur
class jurnal:
    def __init__(self,nama,peneliti):
        self.nama=nama
        self.peneliti=peneliti
    def daftar_peneliti(self):
        for peneliti in self.peneliti:
            print(peneliti.nama,peneliti.umur)

peneliti1=peneliti("abdu",30)
peneliti2=peneliti("hamka",23)

Jurnal= jurnal("makhluk hidup",[peneliti1,peneliti2])
Jurnal.daftar_peneliti() 