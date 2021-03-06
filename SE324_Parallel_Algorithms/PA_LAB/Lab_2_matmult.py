import random

def GetMatrix(m1,m2):
    mat = []
    for i in range(m1):
        mat.append(random.sample(range(25),m2))
    return mat

def Multiply(M1, M2):
    if( len(M1[0]) != len(M2)):
        print("Incompatible Matrices, returning Null")
        return None
    res = []
    for i in range(len(M1)):
        res.append([0 for j in range(len(M2[0]))])

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            res[i][j] = 0
            for k in range(len(M1[0])):
                res[i][j] += M1[i][k]*M2[k][j]
    return res

def main():
    print("Enter Dimensions of matrix A : ")
    m1,m2 = map(int, input().split())
    print("Generating Matrix 1 :")
    M1 = GetMatrix(m1,m2)
    for i in M1:
        print(i)
    print("Enter Dimensions of matrix A : ")
    m1,m2 = map(int, input().split())
    print("Generatig Matrix 2 : ")
    M2 = GetMatrix(m1,m2)
    for i in M2:
        print(i)
    print("Multiplying M1 and M2")
    res = Multiply(M1, M2)
    print("The result is : ")
    for i in res:
        print(i)

if __name__ == '__main__':
    main()