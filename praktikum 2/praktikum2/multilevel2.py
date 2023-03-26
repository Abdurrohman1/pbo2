#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)

class nakes:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class dokter(nakes):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary
        
    def get_details(self):
        super().get_details()
        print(f"ID: {self.id}, Salary: {self.salary}")
        
class spesialis(dokter):
    def __init__(self, name, age, id, salary, praktek):
        super().__init__(name, age, id, salary)
        self.praktek = praktek
        
    def get_details(self):
        super().get_details()
        print(f"praktek: {self.praktek}")