import data
import time

def insertionSort(lst):
    n = len(lst)
    start_time = time.perf_counter()
    cont = 0
    for i in range(n - 1):
        for j in range(i + 1, 0, -1):
            cont += 1
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break

    execution_time = time.perf_counter() - start_time
    print(f"-> Tempo: {execution_time:.5f} segundos")
    print(f"-> Quantidade de iteracoes: {cont}")
    return lst

for i in range(len(data.lstInput)):
    lst = data.lstInput[i]
    print(f"-> Lista {i + 1}: {lst}")
    lst = insertionSort(lst)
    print(f"-> Lista {i + 1} ordenada: {lst}\n\n")
