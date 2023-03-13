class Air_mineral:
    def __init__(self,merk,ukuran):
        self.merk= merk 
        self.ukuran=ukuran
        
    def info(self):
        print(f"air_mineral {self.merk}  berukuran {self.ukuran}")
        
air_mineral=Air_mineral("crystaline","600ml")
air_mineral.info()