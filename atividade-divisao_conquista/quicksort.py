class MergeSort:

    def mergeSortAsc(self, vetor):
        print(vetor)

        if len(vetor) > 1:
            #divisao
            mid = len(vetor)//2
            left = vetor[:mid]
            right = vetor[mid:]

            self.mergeSortAsc(left)
            self.mergeSortAsc(right)
            # conquista -> junção e ordenação dos elementos
            i = j = k = 0
            while((i < len(left)) and (j < len(right))):
                if(left[i] < right[j]):
                    vetor[k] = left[i]
                    i += 1
                else:
                    vetor[k] = right[j]
                    j += 1
                k += 1

            while(i < len(left)):
                vetor[k] = left[i]
                i += 1
                k += 1

            while(j < len(right)):
                vetor[k] = right[j]
                j += 1
                k += 1

    #
    def mergeSortDesc(self, vetor):
        if len(vetor) > 1:
            #divisao
            mid = len(vetor)//2
            left = vetor[:mid]
            right = vetor[mid:]

            self.mergeSortDesc(left)
            self.mergeSortDesc(right)
            # conquista -> junção e ordenação dos elementos
            i = j = k = 0
            while((i < len(left)) and (j < len(right))):
                if(left[i] > right[j]):
                    vetor[k] = left[i]
                    i += 1
                else:
                    vetor[k] = right[j]
                    j += 1
                k += 1

            while(i < len(left)):
                vetor[k] = left[i]
                i += 1
                k += 1

            while(j < len(right)):
                vetor[k] = right[j]
                j += 1
                k += 1

class QuickSort:
    def quick_sort_asc(self, vetor, ini=0, fim = None):
        fim = fim if fim is not None else len(vetor)
        if ini < fim:
            novo_ponto = self.particao(vetor, ini, fim)
            self.quick_sort_asc(vetor, ini, novo_ponto)
            self.quick_sort_asc(vetor, novo_ponto + 1, fim)
        return vetor

    def particao(self, vetor, ini, fim):
        pivo = vetor[fim - 1]
        for i in range(ini, fim):
            if vetor[i] > pivo:
                fim += 1
            else:
                fim += 1
                ini += 1
                vetor[i], vetor[ini - 1] = vetor[ini - 1], vetor[i]
        return ini - 1
# -----------------------
vetor = [999, 20, 30, 90, 45, 10, 6, 8, 40, 25, 36, 98, 102, 360, 1]

objeto = QuickSort()
objeto.quick_sort_asc(vetor, 0 , len(vetor))
print(vetor)
# objeto.mergeSortDesc(vetor)
# print(vetor)