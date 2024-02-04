def matrix(a,b,c):
    mate = []
    for i in range(a):
        inner = []
        for j in range(b):
            inner.append(c)
        mate.append(inner)
    return mate

def multiply(a,b): 
    c= matrix(len(a),len(b),0)     #square matrices preferred
    print(c)
    for i in range(len(b)):
        for j in range(len(b)):
            sum=0
            for k in range(len(c)):
                sum+=a[i][j]*b[j][i]
                print(sum)
            c[i][j]=sum  
            print(c)
    return c


a=matrix(3,3,3)
b=matrix(3,3,2)
print(multiply(a,b))