# Classe que representa cada paciente (Cartão)/Class that represents each patient (card)
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

# Classe de Lista Encadeada/Linked list class
class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contador_verde = 1 #Contador para verde começa no 1/Counter to green starts at 1
        self.contador_amarelo = 201 #Contador para amarelo começa no 201/Counter to yellow starts at 201

# Insere novo paciente no fim da lista (sem prioridade)/Insert new patient at the end of the list (no priority)
    def inserirsemprioridade(self, novo_nodo):
        if self.head is None:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

# Insere paciente com prioridade (cartão amarelo)/Insert patient with priority (yellow card)
    def inserircomprioridade(self, novo_nodo):
        if self.head is None or self.head.cor == "V":
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == "A":
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

# Inserir um novo paciente baseado na cor escolhida e numeração automática/Insert a new patient based on input color and automatic numbering
    def inserir(self):
        cor = input("Digite a cor do cartão (A para Amarelo ou V para Verde): ").strip().upper()
        if cor not in ['A', 'V']:
            print("Cor inválida. Tente novamente.")
            return

        if cor == 'A':
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        else:
            numero = self.contador_verde
            self.contador_verde += 1

        novo_nodo = Nodo(numero, cor)

# Se a lista estiver vazia, coloque novo paciente como primeiro/If the list is empty, set new patient as head
        if self.head is None:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirsemprioridade(novo_nodo)
        else:
            self.inserircomprioridade(novo_nodo)

        print(f"Paciente com cartão {cor}{numero} adicionado à fila.")

# Printe a lista de espera inteira do primeiro ao último/Print the entire waiting list from head to last patient
    def imprimirlistaespera(self):
        if self.head is None:
            print("A lista de espera está vazia.")
        else:
            print("\n--- Lista de Espera ---")
            atual = self.head
            while atual:
                print(f"Cartão: {atual.cor}{atual.numero}")
                atual = atual.proximo

# Remova o primeiro paciente na fila e o chame para atendimento/Remove the first patient in the queue and call them for attendance
    def atenderpaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            print(f"\nChamando paciente com cartão {self.head.cor}{self.head.numero} para atendimento.")
            self.head = self.head.proximo

# Menu principal do sistema/Main menu of the system
def menu():
    fila = ListaEncadeada()
    while True:
        print("\nMain Menu")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            fila.inserir()
        elif opcao == '2':
            fila.imprimirlistaespera()
        elif opcao == '3':
            fila.atenderpaciente()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Iniciar o programa/Start the program
if __name__ == "__main__":
    menu()
