pos = 0

def search(list,n):
    for i in range(len(list)):
        if(list[i] == n):
            globals()['pos'] = i
            return True
        
    



list =  [34,5,2,87,65,90]
n  = int(input("Enter the number to search: "))

if search(list,n):
    print("Found At :",pos+1)
else:
    print("Not Found")