#Nama :Abdurrohman
#Nim  :210511035
#Kelas:R1(TI21A)
class fahrenheit:
    def __init__(self,f):
        self.fahrenheit=f
    
    def fahrenheit_to_celcius(self):
        F = (5/9) * (self.fahrenheit-32)
        return F
    
    def fahrenheit_to_reamur(self):
        R = (4/9) * (self.fahrenheit-32)
        return R
    
    def fahrenheit_to_kelvin(self):
        K = (self.fahrenheit-32)* 5/9 + 273
        return K
F_C = 75
FahrenheitA = fahrenheit(F_C)
print("Konversi",F_C, "derajat fahrenheit adalah:", {FahrenheitA.fahrenheit_to_celcius()}, "derajat Celcius\n")

F_R = 60
FahrenheitB = fahrenheit(F_R)
print("Konversi",F_R, "derajat Fahrenheit adalah", {FahrenheitB.fahrenheit_to_reamur()}, "derajat Reamur\n")

F_K = 90
FahrenheitC = fahrenheit(F_K)
print("Konversi",F_R, "derajat Fahrenheit adalah", {FahrenheitC.fahrenheit_to_kelvin()}, "derajat Kelvin\n")
print("-"*100)
#Nama :Abdurrohman
#Nim  :210511035
#Kelas:R1(TI21A)
class reamur:
    def __init__(self,r):
            self.reamur=r
    
    def reamur_to_celcius(self):
        F = (5/4) * (self.reamur)
        return F
    
    def reamur_to_fahrenheit(self):
        R = (9/4) * self.reamur+32
        return R
    
    def reamur_to_kelvin(self):
        K = (self.reamur/0.8) + 273
        return K
R_C = 75
ReamurA = reamur (R_C)
print("Konversi",R_C, "derajat reamur adalah:", {ReamurA.reamur_to_celcius()}, "derajat Celcius\n")

R_F = 60
ReamurB = reamur (R_F)
print("Konversi",R_F, "derajat reamur adalah", {ReamurB.reamur_to_fahrenheit()}, "derajat Fahrenheit\n")

R_K = 90
ReamurC = reamur (R_K)
print("Konversi",R_K, "derajat reamur adalah", {ReamurC.reamur_to_kelvin()}, "derajat Kelvin\n")
print("-"*100)
#Nama :Abdurrohman
#Nim  :210511035
#Kelas:R1(TI21A)
class kelvin:
    def __init__(self, k):
        self.kelvin = k

    def kelvin_to_fahrenheit(self):
        F =  (self.kelvin*9/5) - 459.67
        return F
    
    def kelvin_to_reamur(self):
        R = (4/5) * (self.kelvin-273)
        return R
    
    def kelvin_to_celcius(self):
        K = self.kelvin - 273.15
        return K
    
k_F = 75
KelvinA = kelvin(k_F)
print("Konversi",k_F, "derajat kelvin adalah:", {KelvinA.kelvin_to_fahrenheit()}, "derajat Farenheit\n")

k_R = 60
kelvinB = kelvin(k_R)
print("Konversi",k_R, "derajat kelvin adalah", {kelvinB.kelvin_to_reamur()}, "derajat Reamur\n")

k_C = 90
kelvinC = kelvin(k_C)
print("Konversi",k_R, "derajat kelvin adalah", {kelvinC.kelvin_to_celcius()}, "derajat celcius\n")
print("-"*100)




