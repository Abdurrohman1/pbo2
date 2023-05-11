class Pekerja:
    def __init__(self, name):
        self.name = name

    def gaji(self):
        raise NotImplementedError

class Supervisor(Pekerja):
    def gaji(self):
        return ' Rp 7.000.000'

class Manajer(Pekerja):
    def gaji(self):
        return ' Rp 4.000.000'

class Mekanik(Pekerja):
    def gaji(self):
        return ' Rp 3.500.000'

parapekerja = [Supervisor('abdurrohman'), Manajer('adi'), Supervisor('gempar'),
Mekanik('Anton')]

for pekerja in parapekerja:
    print(pekerja.name + ': ','Gaji/bulan' + pekerja.gaji())