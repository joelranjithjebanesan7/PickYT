def list_max():
    array = []
    array_length = int(input("Enter the length of array : "))
    operation_num = int(input("Enter no of operartions to perform : "))
    values_num = int(input("Enter num of element to be used : "))
    for i in range(array_length):
        array.append(0)
    for j in range(operation_num):
        a = int(input("Enter the start index : "))
        k = int(input("Enter the end index : "))
        v = int(input("Enter the value for the operation : "))
        for l in range(a-1,k):
            array[l] += v
        list_max = array[0]
        for i in range(1,array_length):
            if array[i] > list_max :
                list_max = array[i]
    
    return list_max

print (list_max())
