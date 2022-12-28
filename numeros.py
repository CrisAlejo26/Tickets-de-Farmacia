# Generador de turnos

# ! Generador de turnos Perfumeria
def numerosPerfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"

# ! Generador de turnos Farmacia
def numerosFarmacia():
    for n in range(1, 10000):
        yield f"F - {n}"
        
# ! Generador de turnos Cosmetica
def numerosCosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

p = numerosPerfumeria()
f = numerosFarmacia()
c = numerosCosmetica()

def decorador(rubro):
    
    print("\n" + "*" * 23)
    print("Su numero es: ")
    if rubro == "F":
        print(next(p))
    elif rubro == "F":
        print(next(c))
    else:
        print(next(c))
    print("Aguarde y sera atentido")
    print("*" * 23 + "\n")