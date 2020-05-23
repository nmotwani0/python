for i in range(4):
    for j in range(i,4):
        print(j+1 , end="")

    print()

print()


for i in range(4):
    for j in range(4):
        print("#",end="")

    print()

print()

for i in range(4):
    for j in range(i+1):
        print("#",end="")

    print()

print()


for i in range(4):
    for j in range(4-i):
        print("#",end="")

    print()

print()

list1 = ['A','B','C','D']
list2 = ['P','Q','R']

for i in range(4):
    for k in range(i+1):
        print(list1[k],end="")
    for j in range(3-i):
        print(list2[j],end="")

    print()

print()

str="1234"
for i in range(4):
    print(str[i:])