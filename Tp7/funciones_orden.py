def ord_buble(arreglo):
    n = len(arreglo)

    for i in range(n-1):       
        for j in range(n-1-i): 
            if arreglo[j] > arreglo[j+1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1] 
                arreglo[j+1] = aux

def ord_selection(arreglo):
    for i in range(len(arreglo) - 1):        
        menor = i 
        aux = 0

        for j in range(i + 1, len(arreglo)): 
            if arreglo[j] < arreglo[menor]:
                menor = j

        if menor != i:
            aux = arreglo[menor]
            arreglo[menor] = arreglo[i]
            arreglo[i] = aux

def ord_insert(array):
    for i in range(len(array)):
        for j in range(i,0,-1):
            if(array[j-1] > array[j]):
                aux = array[j]
                array[j] = array[j-1]
                array[j-1] = aux

def ord_count(array):
   new_array = [0 for i in range(len(array))]
   count = [0 for i in range(10)]
   
   for i in array: count[i] += 1
   for i in range(1, 10): count[i] += count[i-1]
   
   for i in range(len(array)):
      new_array[count[array[i]] - 1] = array[i]
      count[array[i]] -= 1
      
   return new_array

def merge_sort(array):
   if len(array) < 2:
      return array
   else:
        middle = len(array) // 2
        right = merge_sort(array[:middle])
        left = merge_sort(array[middle:])
        return merge(right, left)
    
def merge(array1, array2):
    i, j = 0, 0
    result = []
 
    while(i < len(array1) and j < len(array2)):
        if (array1[i] < array2[j]):
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
 
    result += array1[i:]
    result += array2[j:]
    return result