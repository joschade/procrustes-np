from procrustes_np import orthogonal_procrustes
from numpy.random import random
import numpy as np

A = random((3,85))

#rotation
B = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]) @ A

# rotation and reflection
C = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]]) @ A

Omega_B, t_B, d_B = orthogonal_procrustes(A,B)
Omega_C, t_C, d_C= orthogonal_procrustes(A,C, reflection=False)