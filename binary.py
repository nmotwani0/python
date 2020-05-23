pos = -1

def search(list,n):

    l=0
    u= len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False




list =  [34,5,2,87,65,90]
n  = int(input("Enter the number to search: "))

if search(list,n):
    print("Found At :",pos+1)
else:
    print("Not Found")