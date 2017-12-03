import numpy as np

def Gauss(A, b): 
    n = len(A)

    # assert len(b) == n

    def pivot(piv_row):
        max = A[piv_row][piv_row]
        maxRow = piv_row
        for row in range(piv_row + 1, n):
            if A[row][piv_row] > max:
                max = A[row][piv_row]
                maxRow = row
        temp = list(A[maxRow])
        A[maxRow] = A[piv_row]
        A[piv_row] = temp
        temp = list(b[maxRow])
        b[maxRow] = b[piv_row]
        b[piv_row] = temp

    for pivot_row in range(0, n-1):
        pivot(pivot_row)
        for row in range(pivot_row + 1, n):
            multiplier = A[row][pivot_row] / A[pivot_row][pivot_row]

            for col in range(pivot_row, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            b[row] = b[row] - multiplier * b[pivot_row]
    
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k] / A[k,k]

    while k >= 0 :
        x[k] = (b[k] - np.dot(A[k, k+1:], x[k+1:])) / A[k,k]
        k = k - 1
    return x

def main():
    A = np.array([[2.0,-3.0,0.0],[4.0,-5.0,1.0],[2.0,-1.0,-3.0]])
    b =  np.array([[3.0],[7.0],[5.0]])
    print(Gauss(np.copy(A), np.copy(b)))

if __name__ == '__main__':
    main()