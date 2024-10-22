str=input("enter string: ")
a=str.split()
fx=int(input("coding or decoding(1/2): "))
if fx==1:

    if len(a)>=3:
        c=""
        l=list(a)
        b=l.pop(0)
        l.append(b)
        for i in l:
            c+=i
        print(c)
    else:
        a=a[::-1]
        print(str(a))
elif fx==2:
    if len(a)>=3:
        c=""
        l=list(a)
        b=l.pop(0)
        l.append(b)
        for i in l:
            c+=i
        print(c)
    else:
        a=a[::-1]
        print(str(a))
else:
    print("enter valid function")