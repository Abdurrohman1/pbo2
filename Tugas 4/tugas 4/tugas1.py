class Profesor:
    def __init__(self,nama,umur):
        self.nama=nama 
        self.umur=umur
        
class Riset:
    def __init__(self,nama,Profesor):
        self.nama=nama
        self.Profesor=Profesor
    
    def daftar_profesor(self):
        for Profesor in self.Profesor:
            print(Profesor.nama,Profesor.umur)
        
profesor1=Profesor("abdu",21)
profesor2=Profesor("gempar",23)

riset=Riset("makhluk hidup",[profesor1,profesor2])
riset.daftar_profesor()