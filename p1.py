import numpy as np
A=np.random.randint(10,size=(3,3))
print(A)
inverse=np.linalg.inv(A)
print("inverse of matrix:",inverse)
rank=np.linalg.matrix_rank(A)
print("Rank of matrix:",rank)
determinant=np.linalg.det(A)
print("Determinant of matrix",determinant)
new_A=A.reshape(-1)
print("transformed array",new_A)
v,w=np.linalg.eig(A)
print("eigen values",v)
print("eigen vectors",w)


