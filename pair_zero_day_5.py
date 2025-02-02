def find_pair_with_zero_sum(arr):
    num_set = set()  
    for num in arr:
        if -num in num_set:  
            return (num, -num)
        num_set.add(num)  
    return "No Pair Found"


arr1 = [3, 1, -4, 6, -3, 8]
arr2 = [1, 2, 3, 4]

print(find_pair_with_zero_sum(arr1))  
print(find_pair_with_zero_sum(arr2))  
