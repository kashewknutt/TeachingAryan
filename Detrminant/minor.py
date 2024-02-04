def matrix(a,b,c):
    mate = []
    for i in range(a):
        inner = []
        for j in range(b):
            inner.append(c)
        mate.append(inner)
    return mate

def minor(mat,i,j):
    a=b=0
    new = matrix(len(mat)-1,len(mat)-1,0)
    for x in range(len(mat)):
        if x == i:
            continue

        for y in range(len(mat)):
            if y == j:
                continue
            new[a][b]=mat[x][y]
            b+=1
        b=0
        a+=1    
    return new
a=[[1,2,3],[4,5,6],[7,8,9]]
print(minor(a,3,3))
      