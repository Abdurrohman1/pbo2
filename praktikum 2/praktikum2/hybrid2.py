#Nama :Abdurrohman
#Nim  :210511035
#kelas:R1(TI21A)
print('\nHybrid Inheritance\n\n')

# Hybrid Inheritance
class vehicle:
    
    def __init__(self,name,model):
        self.name = name
        self.model = model
        
    def show_details(self):
        print(f'\nName : {self.name}')
        print(f'Model : {self.model}')
                
class bike(vehicle):
    
    # Inherit Properties and Override
    def __init__(self,name,model,type):
        super().__init__(name,model)
        self.type = type
    
    # Inherit Behavior and Override
    def show_details(self):
        super().show_details()
        print(f'Album : {self.type}\n')
    
    # Method of Derived Class
    def info(self):
        print(f'{self.name} {self.model} mengeluarkan type terbarunya yaitu {self.type}')
        

class car(bike,vehicle):
    
    def info(self):
        print('\n\n\t\t\tNEWS!!!\t\t\t\n\n')

bajaj = car("honda","civic","type r")
bajaj.show_details()
bajaj.info()

motor1 = bike("mitsubishi","evo","2")
motor1.info()
motor1.show_details()