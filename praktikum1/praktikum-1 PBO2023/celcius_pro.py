#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)

class Celcius:
    @staticmethod
    def celcius_to_fahrenheit (C):
       F=(9/5)* C + 32
       return F
    
    @staticmethod
    def celcius_to_reamur(C):
        R = 4/5 * C 
        return R
    @staticmethod
    def celcius_to_kelvin (C):
        k = C + 273
        return k
    
C = 75 
F = Celcius.celcius_to_fahrenheit(C) 
print ("konversi",C,"derajat Celcius adalah:",F,"derajat Fahrenheit")

C = 60
R = Celcius.celcius_to_reamur(C)
print("konversi",C,"derajat celcius adalah:",R,"derajat Reamur")

C = 90
K= Celcius.celcius_to_kelvin(C)
print("konversi",C,"derajat Celcius adalah:",K,"derajat Kelvin")