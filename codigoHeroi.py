from dataclasses import dataclass

@dataclass
class Heroi:
    nome: str
    poder: str
    idade: int
    altura: float
    ativo: bool
    
homem_aranha = Heroi("Homem aranha", "sentido aranha", 16, 1.76, True)
cavaleiro_da_lua = Heroi("Cavaleiro da lua", "konshu", 40, 1.82, True)
batman = Heroi("Batman", "Batmóvel", 0, 1.85, True)
 
lista_de_herois = []
lista_de_herois.append(homem_aranha)
lista_de_herois.append(cavaleiro_da_lua)
lista_de_herois.append(batman)
 
print(lista_de_herois)

digite = int(input("\nQual heroi você quer? \n1 - homem aranha \n2 - cavaleiro da lua \n3 - batman\n"))
print(lista_de_herois[digite-1])