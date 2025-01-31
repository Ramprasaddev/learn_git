def movingelements(arr) :
	non_index=0
	leng=len(arr) 
	for i in range(leng) : 
		if arr[i]!=0 :
			arr[non_index]=arr[i]
			non_index+=1
	for i in range(non_index,leng) :
		arr[i]=0
	return print(arr)

arr=[0,1,2,0,3]
movingelements(arr)
