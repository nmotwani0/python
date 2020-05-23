from array import array

def quickSort(toSortArray):
    
    
    n = len(toSortArray) 
    if(n<=1):
        return toSortArray
    else:
        pivot = toSortArray.pop()
        leftArray = array('i',[])
        rightArray = array('i',[])
        resultArray = array('i',[])

        for i in toSortArray:
            if i>pivot:
                rightArray.append(i)
            else:
                leftArray.append(i)

        resultArray.extend(quickSort(leftArray))
        resultArray.append(pivot)
        resultArray.extend(quickSort(rightArray))

    return resultArray

myArray = array('i',[43,78,23,76,5,12,67,43,98,67])
print(quickSort(myArray))

    