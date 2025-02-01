def merged_array(arr1,arr2,m,n):
    p1=m-1
    p2=n-1
    p=(m+n)-1
    while (p1>=0 and p2>=0) :
        if arr1[p1] > arr2[p2] :
            arr1[p]=arr1[p1]
            p1 -=1
        else :
            arr1[p]=arr2[p2]
            p2 -=1
        p -=1
    while p2>=0 :
        arr1[p]=arr2[p2]
        p-=1
        p2-=1
    return print(arr1)

arr1=[1,2,3,0,0,0]
arr2=[3,5,18]
merged_array(arr1,arr2,3,3)
