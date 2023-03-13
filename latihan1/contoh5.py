class Kereta:
    def __init__(self, lokomotiv, tujuan):
        self.lokomotiv = lokomotiv
        self.tujuan = tujuan
    def info(self):
        print(f"Lokomotif: {self.lokomotiv}\nTujuan: {self.tujuan}")
KeretaA = Kereta("PT KAI Prujakan", "Cirebon - tegal")
KeretaA.info()