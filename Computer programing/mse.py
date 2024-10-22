#factorial recursion
def fac(n):
        if n<2:
            return n
        else:
            return n+fac(n-1)

print(fac(4))


#fibonacci recursion
def fib(x):
    if x==0 or x==1:
        return 'a'
    else:
        a=fib(x-1)+fib(x-2)
        print(fib(x-1),'+',fib(x-2))
        return a
print(fib(4))

