import numeros

def preguntar():
    
    print("Bienvenido a Farmacia Python")
    
    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            miRubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(miRubro)
        except ValueError: # Error de valor
            print("Esa no es una opcion valida")
        else:
            break
    numeros.decorador(miRubro)

def inicio():
    while True:
        preguntar()
        try:
            otroTurno = input("Quieres sacar otro turno: [S] [N] ").upper()
            ["S", "N"].index(otroTurno) # Busca que si este la opcion que es
        except:
            print("Esa no es una opcion valida")
        else:
            if otroTurno == "N":
                print("Gracias por su visita")
                break

inicio()