class BubbleSort:

    def ordenaCrescente(self, vetor):
        trocado = True
        elementos = len(vetor) - 1

        while elementos > 0 and trocado:
            trocado = False
            for i in range(elementos):
                if(vetor[i] > vetor[i+1]):
                    trocado = True
                    temp = vetor[i]
                    vetor[i] = vetor[i+1]
                    vetor[i+1] = temp
            elementos = elementos - 1
            

    def ordenaDecrescente (self, vetor):
        trocado = True
        elementos = len(vetor) -1
        
        while elementos > 0 and trocado:
            trocado = False
            for i in range(elementos):
                if(vetor[i] < vetor[i+1]):
                    trocado = True
                    temp = vetor[i]
                    vetor[i] = vetor[i+1]
                    vetor[i+1] = temp
            elementos = elementos - 1

            
# -----------------------
vetor = [20, 30, 90, 45, 10, 6, 8, 40, 25, 36, 98, 102, 360, 1]
bubble = BubbleSort()
bubble.ordenaCrescente(vetor)
print(vetor)
bubble.ordenaDecrescente(vetor)
print(vetor)


# visualgo.net 
# using site in class for view code in run