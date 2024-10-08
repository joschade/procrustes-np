from numpy import matmul, mean, array, shape
from numpy.linalg import svd, det

def orthogonal_procrustes(A: array, B: array, reflection = False) -> array:
    """
    :param A: matrix to be matched on B by rigid motion
    :param B: matrix to be matched by A
    :return Omega: rigid motion matrix Omega such that Omega*A =~ B
    """
    assert A.shape == B.shape, "arrays A and B must be of equal shape"

    # centering
    a = mean(A, axis=1)
    b = mean(B, axis=1)

    A_centered = (A.transpose() - a).transpose()
    B_centered = (B.transpose() - b).transpose()

    # perform SVD
    U, _, Vh = svd(matmul(B_centered, A_centered.transpose()))

    # make sure rigid motion (no reflection):
    if not reflection:
        if det(Vh) < 0.: Vh[0] = -Vh[0]

    # compute Omega
    Omega = matmul(U, Vh)

    return Omega

