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


    def mergeSorrtDesc(self, vetor):
        pass

# -----------------------
vetor = [999, 20, 30, 90, 45, 10, 6, 8, 40, 25, 36, 98, 102, 360, 1]

objeto = MergeSort()
objeto.mergeSortAsc(vetor)
print(vetor)
# insertion.ordenaDecrescente(vetor)
# print(vetor)