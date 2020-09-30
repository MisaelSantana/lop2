class SelectionSort:
    def ordenaCrescente(self, vetor):
        tamanho = len(vetor)
        for i in range(tamanho):
            minimo_indice = i
            for j in range(i+1, tamanho):
                if vetor[minimo_indice] > vetor[j]:
                    minimo_indice = j

            vetor[i], vetor[minimo_indice] = vetor[minimo_indice], vetor[i]

    def ordenaDecrescente(self, vetor):
        tamanho = len(vetor)
        for i in range(tamanho):
            minimo_indice = i
            for j in range(i+1, tamanho):
                if vetor[minimo_indice] < vetor[j]:
                    minimo_indice = j

            vetor[i], vetor[minimo_indice] = vetor[minimo_indice], vetor[i]


# --------------------
vetor = [20, 30, 90, 45, 10, 6, 8, 40, 25, 36, 98, 102, 360, 1]
Selection = SelectionSort()
Selection.ordenaCrescente(vetor)
print(vetor)
Selection.ordenaDecrescente(vetor)
print(vetor)
