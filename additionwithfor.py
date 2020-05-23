from numpy import array

arr1 = array([1,4,7,10])
arr2 = array([40,5,4,43])

for i in range(len(arr1)):
    arr3 = arr1[i]+arr2[i]
    print(arr3,end=" ")