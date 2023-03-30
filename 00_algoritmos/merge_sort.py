from multiprocessing import Process
from time import sleep

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        process_a = Process(target=mergeSort, args=(sub_array1,))
        process_b = Process(target=mergeSort, args=(sub_array2,))
        process_a.start()
        process_b.start()
        process_a.join() 
        process_a.join() 
        sleep(1)

        mergeSort(sub_array1)
        mergeSort(sub_array2)
         
        i = j = k = 0
 
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
 
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

    print('Processo rodando... array com len',len(arr))
 



if __name__ == '__main__':
    arr = [10, 9, 2, 4, 6, 13, 89, 3, 0, 12]
    print('Código iniciado...')
    mergeSort(arr)
    print(arr)
    print('Código finalizado.')
