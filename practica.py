
class donas():
    tipo=""
    cantidad=0
    precio=0
    preciototal=0
    sabor=""
    glaseado=""
    topping=""

    
    def __init__(self):
        self.tipo= ""
        self.cantidad=0
        self.precio=0
        self.preciototal=0
        self.sabor=""
        self.glaseado=""
        self.topping=""

    def tomarorden(self):
        if(self.tipo == "g" or self.tipo=="grande"):
            self.precio=(self.cantidad * 0.25)
            print(f"El tamano de la dona es grande y llevas la cantidad de {self.cantidad}")
        elif(self.tipo=="p" or self.tipo=="pequeña"):
            self.precio=(self.cantidad * 0.15)
            print(f"El tamano de la dona es pequena y llevas la cantidad de {self.cantidad}")
        else:
            print("No lo escribiste bien, intenta escribiendo todo con minusculas")
    
    def registro(self):
        self.tipo=input(f"Elija el tamaño de las donas g/p > ").lower()
        self.cantidad=int(input("Elija la cantidad de unidades que llevara > "))
        self.sabor= input(f"Elija el sabor de la masa > ")
        self.glaseado= input(f"Elija el color del glaseado > ")
        self.topping= input(f"Elija el topping > ")

    def mostrardato(self):
        print(f"GRACIA POR COMPRARME")
        self.tomarorden()
        print(f"Precio a pagar: ${self.precio}")
        print(f"El color del glaseador es {self.glaseado}")
        print(f"El topping es {self.topping}")

orden=donas()
orden.registro()
print("------------------------------------------")
orden.mostrardato()
print("------------------------------------------")



