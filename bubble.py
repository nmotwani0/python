
vals = [4,76,23,90,56,12]
print("Initial List:",vals)
for i in range(len(vals)):
   for j in range(i+1,len(vals)):
        if vals[i]>=vals[j]:
            vals[i],vals[j]=vals[j],vals[i]

print("Sorted List:",vals)