def second_largest(arr):
    largest=-1
    secondlargest=-1

    if len(arr) < 2 :
        return -1


    for i in range(len(arr)) :
        if arr[i] >largest :
            secondlargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>secondlargest :
            secondlargest=arr[i]
    return secondlargest


array=[23,54,66,64,55,75]
print(second_largest(array))
