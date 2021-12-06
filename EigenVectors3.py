import  numpy as np
#create a matrix

# Create matrix
matrix = np.array([[1, 2, 3],
                   [3, 2, 1],
                   [1, 0, -1]])

# print (matrix.shape)
#Finding the Eigenvalue and Eigenvectors of matrix

w, v = np.linalg.eig(matrix)
print ('Eigenvalues are: ', w)
print ('Eigenvectors per column are: ', v)


