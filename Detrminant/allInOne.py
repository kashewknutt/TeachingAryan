def matrix(a,b,c):
    mate = []
    for i in range(a):
        inner = []
        for j in range(b):
            inner.append(c)
        mate.append(inner)
    return mate


def betterMinor(a,i,j):
    A=b=0
    new=matrix(len(a)-1,len(a)-1,0)
    arrA=[]
    arrB=[]
    arrC=[]
    for x in range(len(a)):
        arrA.append(x)
        arrB.append(x)
        arrC.append(x)
    #print("arrA: ",arrA)
    arrA.remove(i)
    #print("arrA:",arrA)
    for p in arrA:
        arrB.remove(j)
        #print("arrB:",arrB)
        for q in arrB:
            #print("p:",p,"q:",q)
            new[A][b]=a[p][q]
            #print("New changed: ",new)
            arrB=arrC
            #print("arrB",arrB)
            #print("arrC",arrC)
            #print("A,b: ", A,b)
            b+=1
        arrA,arrC=[],[]
        for x in range(len(a)):
            arrA.append(x)
            arrC.append(x)
        b=0
        A+=1
    return new    

def det(a):
    if len(a)==1:
        ans = a[0][0]
    else:
        ans = 0
        for j in range(len(a)):
            #print("minor",betterMinor(a,0,j))
            ans += ((-1)**(j))*det(betterMinor(a,0,j))*a[0][j]
            #print("ans",ans)
    return ans

print("Hello Noobs!")
print("PHir aagaye determinant nikalne?")
size = 'a'
while size.isdigit() == False:
    size = input("Enter size:")
n = int(size)

mat = matrix(n,n,0)
choice = 'a'
for a in range(len(mat)):
    for b in range(len(mat)):
        print("Your matrix is:")
        for i in mat:
            for j in i:
                print(j," ",end='')
            print()
        while choice.isdigit() == False:
            choice = input("Enter values in order:")
        mat[a][b] = float(choice)
print(det(mat))


