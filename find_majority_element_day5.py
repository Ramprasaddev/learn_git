def majority(arr) :
    count=0
    for i in range(len(arr)) :
        for j in range(len(arr)) :
            if arr[i] == arr[j] :
                count +=1
    if count >(len(arr)/2 ) :
        print(arr[i])
    return -1
array=[1,1,2,2,2]
majority(array)
