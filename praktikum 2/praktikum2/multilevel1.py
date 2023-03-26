#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("The animal speaks")
class fish(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print("The dog barks")
class shark(fish):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin
    def speak(self):
        print("The shark bite")
