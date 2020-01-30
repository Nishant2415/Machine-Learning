import numpy as np
from sklearn import datasets
from sklearn.datasets import *

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

## Prinat matrix
#print(matrix)
#
##
#print(np.linalg.matrix_rank(matrix))
#
## Calculating the detereminant
#print(np.linalg.det(matrix))
#
## Getting the dignal element
#print('Digonal')
#print(matrix.diagonal())
#
## Return digonal one above the main diagonal
#print(matrix.diagonal(offset=1))
#
## Return digonal one below the main diagonal
#print(matrix.diagonal(offset=-1))
#
#matrix_row = np.array([[1,4],
#                       [2,5]])
#
## Inverting the matrix
#print(np.linalg.inv(matrix_row))
#
#print('')
#print(np.random.seed)

digits = datasets.load_iris()
features = digits.data
target = digits.target
print(features[0])

print('--------------------Regression--------------------')
features1,target1,coefficients = make_regression(n_samples = 100,
                                                 n_features=3,
                                                 n_informative=3,
                                                 n_targets=1,
                                                 noise=0.0,
                                                 coef=True,
                                                 random_state=1)

print('Features matrix\n',features1[:3])
print('Target matrix\n',target1[:3])

print('------------------Classification------------------')

features2,target2 = make_classification(n_samples = 100,
                                                 n_features=3,
                                                 n_informative=3,
                                                 n_redundant=0,
                                                 n_classes=2,
                                                 weights=[.25,.75],
                                                 random_state=1)

print('Features matrix\n',features2[:3])
print('Target matrix\n',target2[:3])

































