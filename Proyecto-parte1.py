import os, readchar
from readchar import key

nombre= input("Introduzca su nombre: ")
print("!Bienvenido a esta nueva aventura, {}!".format(nombre))

while True:
    tecla_1 = readchar.readkey()
    if tecla_1 == key.UP:
        break
    print(tecla_1)
    
def borrar_terminal():
    numveces =0
    print("Borrar terminal")
    while numveces < 50:
        tecla_1 = readchar.readkey()
        if ord(tecla_1)>0:
            os.system('cls' if os.name=='nt' else 'clear')
            numveces=numveces+1
            print(numveces)
            
if __name__=="__main__":
    borrar_terminal() 