#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
class Elektronik:
    def __init__(self, brand, warna):
        self.brand = brand
        self.warna = warna

    def turnOn(self):
        print(self.brand, " Menyala")

class Laptop(Elektronik):
    def __init__(self, brand, warna, OS):
        super().__init__(brand, warna)
        self.OS = OS
    def splashScreen(self):
        print("Menggunakan OS ", self.OS)


lapotpSatu = Laptop("Asus", "Hitam", "Windows")
lapotpSatu.turnOn()  # output: Kitty bergerak
lapotpSatu.splashScreen()  # output: Meow!
