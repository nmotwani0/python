def sub(a,b):
    return a-b


def subtract(func):
    def inner(a,b):
        if(a<b):
             a,b=b,a
        return func(a,b)
    return inner   

sub = subtract(sub) 
res = sub(2,4)
print(res)

print(subtract(sub)(2,4))
  