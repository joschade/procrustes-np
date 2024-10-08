import numpy as np

def orthogonal_procrustes(A: np.array, B: np.array) -> np.array:
    """
    :param A: matrix to be matched on B by rigid motion
    :param B: matrix to be matched by A
    :return: matrix Omega such that Omega*A =~ B
    """

    # perform SVD
    U, Sigma, Vh = np.linalg.svd(B, compute_uv=True)
    # Compute Omega * A (== U*Vh)
    OmegaA = np.matmul(U, Vh)

    #compute Omega * A * pseudoInverse(A) (==Omega)
    Omega = np.matmul(OmegaA, np.linalg.pinv(A))

    return Omega