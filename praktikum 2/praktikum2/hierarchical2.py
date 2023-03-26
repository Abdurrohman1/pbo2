#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
class nakes:
    def __init__(self, name, age, gaji):
        self.name = name
        self.age = age
        self.gaji = gaji
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gaji(self):
        return self.gaji
class dokter(nakes):
    def __init__(self, name, age, gaji, department):
        super().__init__(name, age, gaji)
        self.department = department
    def get_department(self):
        return self.department
class perawat(nakes):
    def __init__(self, name, age, gaji, jabatan):
        super().__init__(name, age, gaji)
        self.jabatan = jabatan
    def get_language(self):
        return self.jabatan
# Hierarchical Inheritance
class SeniorPerawat(perawat):
    def __init__(self, name, age, gaji, jabatan, level):
        super().__init__(name, age, gaji, jabatan)
        self.level = level
    def get_level(self):
        return self.level
