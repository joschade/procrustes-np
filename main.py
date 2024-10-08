import numpy as np

A = np.random.random(size = (3,5))
B = np.random.random(size = (3,5))
U, Sigma , Vh = np.linalg.svd(B, full_matrices=False)
OmegaA = np.matmul(U, Vh)
Omega = np.matmul(OmegaA, np.linalg.pinv(A))


def orthogonal_procrustes(A: np.array, B: np.array) -> np.array:
    """
    :param A: matrix to be matched on B by rigid motion
    :param B: matrix to be matched by A
    :return: matrix Omega such that Omega*A =~ B
    """
    U, Sigma, Vh = np.linalg.svd(B, compute_uv=True)
    OmegaA = np.matmul(U, Vh)
    Omega = np.matmul(OmegaA, np.linalg.pinv(A))

    return Omega