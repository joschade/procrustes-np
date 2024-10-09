import numpy as np
from numpy import matmul, mean, array
from numpy.linalg import svd, det

def orthogonal_procrustes(A: array, B: array, centering = True, reflection = False) -> array:
    """
    :param A: matrix to be matched on B by rigid motion
    :param B: matrix to be matched by A
    :param centering: allow centering of A and B
    :param reflection: allow reflection by Omega
    :return Omega: rigid motion matrix Omega such that Omega*A =~ B
    """

    assert len(A.shape) == 2, "arrays A and B must be 2-dimensional"
    assert A.shape == B.shape, "arrays A and B must be of equal shape"

    if centering:
        # centering
        a = mean(A, axis=1)
        b = mean(B, axis=1)

        A = (A.transpose() - a).transpose()
        B = (B.transpose() - b).transpose()

    # perform SVD on BA^{-1} (pseudo-inverse)
    U, _, Vh = svd(matmul(B, A.transpose()))

    # compute Omega
    Omega = matmul(U, Vh)

    det_Omega = det(Omega)
    # make sure rigid motion (no reflection):
    if not reflection:
        if det(U @ Vh) < 0.:
            D = np.identity(A.shape[0])
            D[-1,-1] = det_Omega
            Omega = U @ D @ Vh
    return Omega

