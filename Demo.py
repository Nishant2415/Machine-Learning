import numpy as np

# Applying operations on matrix
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Creating a function that adds 100 to something
add_100 = lambda i:i+100

# Createing vector function
vectorized_add_100 = np.vectorize(add_100)

# Applying function to all elements of matrix
print(vectorized_add_100(matrix))

# Sa,e this work can be with broadcasting
print(matrix +100)

# Min and max value of matrix
print(np.min(matrix))
print(np.max(matrix))

# Find maximum element in each column
print(np.max(matrix,axis=0))

# Find maximum element in each row
print(np.max(matrix,axis=1))

# Find mean, variance and standard deviation
print('Mean: ',np.mean(matrix))
print('Varience: ',np.var(matrix))
print('Standard deviation: ',np.std(matrix))

print('------------------------------------')
# Reshaping the matrix
matrix2 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12]])

print(matrix2.reshape(2,6))

# Reshape using -1 "as many as needed"
print(matrix2.reshape(-1,2))
print(matrix2.reshape(2,-1))

# Transposing a matrix
print(matrix2.T)

#Flatten matrix






