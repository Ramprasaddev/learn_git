
def moving_zeros(arr) :
    non_index=0
    for i in range(len(arr)) :
        if arr[i] != 0 :
            arr[non_index],arr[i]=arr[i],arr[non_index]
            non_index +=1
    return print(arr)
array=[1,0,3,0,6,8]
moving_zeros(array)
