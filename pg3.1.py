
p = int(input("Enter rows of A: "))
q = int(input("Enter cols of A: "))
A = []
for i in range(p):
    A.append(list(map(int, input().split())))

t = int(input("Enter rows of B: "))
r = int(input("Enter cols of B: "))
B = []
for i in range(t):
    B.append(list(map(int, input().split())))

if(q!=t):
    print("Error! Matrix sizes are not compatible")
    quit()
C = []
for row in range(p):
    curr_row = []
    for col in range(r):
        curr_row.append(0)
    C.append(curr_row)

for i in range(p):
    for j in range(r):
        curr_val = 0
        for k in range(q):
            curr_val += A[i][k]*B[k][j]
        C[i][j] = curr_val

print(C)
