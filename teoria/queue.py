class queue:
    valores = []

    def enqueue(self, valor):
        self.valores.append(valor)

    def dequeue(self):
        if len(self.valores) == 0:
            return "A fila está vazia"
        primeiro = self.valores[0]
        print(primeiro)
        self.valores.pop(0)
        return primeiro

        