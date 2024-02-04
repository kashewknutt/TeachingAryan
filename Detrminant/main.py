from betterMinor import matrix
from determinant import det

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


