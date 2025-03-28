class Stack:
    valores = []

    def push(self, valor):
        self.valores.append(valor)

    def peek(self):
        if len(self.valores) == 0:
            return "A pilha está vazia."
        ultimo = len(self.valores) - 1
        print(self.valores[ultimo])
        return self.valores[ultimo]
    
    def pop(self):
        ultimo_valor = self.peek()
        if len(self.valores) == 0:
            return "Pilha vazia."
        self.valores.pop()
        return ultimo_valor
    
    def showAll(self):
        if self.valores != 0:
            for valor in self.valores:
                print(valor)
    

stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.peek()
stack.showAll()


    