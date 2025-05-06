class Node: #classe para não precisar usar import
    def __init__(self, data): #iterador do nó
        self.data = data #esse data recebe o imput do usuario
        self.next = None
        
class Fila:
    def __init__(self): #metodo de interador
        self.first = None #primeiro
        self.last = None #ultimo
        self.size = 0


    def push(self, data): #metodo de inserir dado na fila
        no = Node(data) #criando nó 
        if self.last is None: #condição para verifica se o ultimo é vazio
            self.last = no #se  for vai receber o varivel nó que foi criado
        else: #se não for vazio o que está apontando recebera no, e o ultimo recebera nó
            self.last.next = no
            self.last = no
        
        if self.first is None: #se o primeiro estiver vazio, vai receber o primeiro dado 
            self.first = no
        
        self.size = self.size + 1

    def pop(self): #método para retirar da fila
        if self.size > 0 : #se o tamanho for maior que 0
            aux = self.first.data #variavel auxiliar para receber a variavel que foi input do usuario
            self.first = self.first.next # a primeira variavel recebe a variavel que está apontando
            if self.first is None: #se a primeira for nulo
                self.last = None # a ultima sera nulo
            self.size = self.size -1 #decrementa em 1 o tamanho 
            return aux # retorna a variavel aux
        raise IndexError("A fila está vazio")
    
    def peek(self): # metodo para retornar o primeiro valor da fila
        if self.size >0:
            aux = self.first.data
            return aux
        raise IndexError("A fila está vazia")
    
    def __repr__(self): #metodo especial que serve para voltar em string os dados da fila para poder mostrar pro usuario
        if self.size > 0:
            aux= ""
            pointer =self.first
            while(pointer):
                aux = aux + str(pointer.data) + ""
                pointer = pointer.next
            return aux
        return "Fila vazia"
    
    def __str__(self):
        return self.__repr__()
    
fila = Fila()
fila.push(1)
fila.push(2)
fila.push(3)
print(fila)
print("o dado que foi retirado é", fila.pop())
print(fila)
print("O primeiro da fila é ",fila.peek())
