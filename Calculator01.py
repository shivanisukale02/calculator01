def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

if __name__=="__main__":
    n1=int(input("Enter a num1"))
    n2=int(input("Enter a num2"))
    print(add(n1,n2))
    print(sub(n1,n2))
    print(mul(n1,n2))
    print(div(n1,n2))
