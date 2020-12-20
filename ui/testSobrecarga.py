from multipledispatch import dispatch

@dispatch(int,int)
def add(x,y):
    return x+y

@dispatch(int)
def add(x):
    return x*x

print(add(9))

