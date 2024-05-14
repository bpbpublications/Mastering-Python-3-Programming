# Program E7x11.py
# Finding Transpose of a given matrix

def transpose(mat1):
    mat1_transpose = [[0, 0, 0],
                      [0, 0, 0]]
    for rows in range(len(mat1)):
        for columns in range(len(mat1[0])):
            mat1_transpose[columns][rows] = mat1[rows][columns]
    return(mat1_transpose)

def main():
    mat0 = [[2, 3],
            [5, 7],   
            [11, 13]]
    mat2=transpose(mat0)
    print("Transposed Matrix is")
    for elements in mat2:
        print(elements)

main()
