from first import matrix
a=matrix(3,3,3)
ans = 0
def minor00(a):
    b=matrix(len(a)-1,len(a)-1,0)
    for i in range(1,len(a)):
        for j in range(1,len(a)):
            b[i-1][j-1]=a[i][j]
    return(b)

def minor01(a):
    b=matrix(len(a)-1,len(a)-1,0)
    for i in range(len(a)):
        
    
def det(a):
    if len(a)==1:
        return ans
    else:
        print(a)

    