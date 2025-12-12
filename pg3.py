p = int(input("Rows in A: "))
q = int(input("Cols in A: "))
A = [list(map(int, input().split())) for _ in range(p)]

t = int(input("Rows in B: "))
r = int(input("Cols in B: "))
B = [list(map(int, input().split())) for _ in range(t)]

if q != t:
    print("Error! Matrix sizes are not compatible")
    quit()

C = [[sum(A[i][k] * B[k][j] for k in range(t)) for j in range(r)] for i in range(p)]

print(C)
