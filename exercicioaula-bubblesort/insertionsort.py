class InsertionSort:
    def ordenaCrescente(self, vetor):
        tamanho = len(vetor)
        for i in range(1, tamanho):
            key = vetor[i]
            indice_anterior = i-1
            while(indice_anterior >= 0 and key < vetor[indice_anterior]):
                vetor[indice_anterior+1] = vetor[indice_anterior]
                indice_anterior -= 1
            vetor[indice_anterior+1] = key

    def ordenaDecrescente(self, vetor):
        tamanho = len(vetor)
        for i in range(1, tamanho):
            key = vetor[i]
            indice_anterior = i-1
            while(indice_anterior >= 0 and key > vetor[indice_anterior]):
                vetor[indice_anterior+1] = vetor[indice_anterior]
                indice_anterior -= 1
            vetor[indice_anterior+1] = key


vetor = [20, 30, 90, 45, 10, 6, 8, 40, 25, 36, 98, 102, 360, 1]
insertion = InsertionSort()
insertion.ordenaCrescente(vetor)
print(vetor)
insertion.ordenaDecrescente(vetor)
print(vetor)