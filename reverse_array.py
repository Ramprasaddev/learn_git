def reverse_array(arr) :
	start=0
	end=len(arr)-1
	while(start<end) :
		tem=arr[start]
		arr[start]=arr[end]
		arr[end]=tem
		start=start+1
		end=end-1
	return print(arr)

array=[1,2,3,4,5]
reverse_array(array)
