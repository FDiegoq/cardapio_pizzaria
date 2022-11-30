class pizza:
    def __init__(self,tamanho,vinicial,pizzafinal):
        self.tamanho=tamanho
        self.vinicial=vinicial
        self.pizzafinal=pizzafinal
    def fazer_pizza(self):
        self.tamanho=input("Qual o tamanho da pizza?(M ou G)").upper()
        if self.tamanho=="M":
            self.vinicial+=20.00
        elif self.tamanho=="G":
            self.vinicial+=25.00
    def add_ingredientes(self):
        ingredientes=[
        ["1.Molho",0.20],
        ["2.Muçarela",1.30],
        ["3.Palmito",1.10],
        ["4.Milho",1.10],
        ["5.Bacon",2.50],
        ["6.Presunto",1.0],
        ["7.Orégano",0.10],
        ["8.Carne de sol",3.50],
        ["9.cheddar",0.50]
        ]

        pizza=[]
        for c  in range (9):
          adicionar=(input("Deseja adicionar {} a sua pizza?(s/n".format(ingredientes[c]))).lower()
          if adicionar=="s":
            for l in range(2):
              self.vinicial+=ingredientes[0][l]
              pizza.append(ingredientes[c][0])
          elif adicionar=="n":
            print("Okay! Obrigado por usar o aplicativo")
        pizza==self.pizzafinal
            

            

        
            


