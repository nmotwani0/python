curr=1
prev=0
fibo=0

print(prev)
while curr<50:
    print(curr)
    fibo = curr + prev
    prev = curr
    curr = fibo
    
