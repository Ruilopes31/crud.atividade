import os
import time
from dataclasses import dataclass
os.system(" cls || clear")


@dataclass
class Funcionario:
    nome:str
    nascimento:str
    cpf:str
    funcao:str

    lista_de_funcionario:[]
    QUANTIDADE_CLIENTES = 1


for i in range:
    print("digite os dados do funcionario:")
    funcionario = Funcionario(
        nome = input("Nome:"),
        nascimento = input("Nascimento:"),
        cpf = input("Cpf:"),
        funcao = input("Funcao:")
    )    

    lista_de_funcionario.append(funcionario)
    print()

def verificar_lista_vazia(lista_de_funcionario):
    if not lista_de_funcionario:
        print("\nA lista está vazia.")
        return True
    return False 

# Função para adicionar nomes.
def adicionar(lista_de_funcionario):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_de_funcionario.append(nome)
    print(f"\n{nome} adicionado com sucesso.")
   
# Função para mostrar nomes.
def mostrar(lista_de_funcionario):
    if verificar_lista_vazia(lista_de_funcionario):
        return
   