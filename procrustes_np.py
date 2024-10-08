from numpy import matmul, mean, array, shape
from numpy.linalg import svd, det

def orthogonal_procrustes(A: array, B: array, centering = True, reflection = False) -> array:
    """
    :param A: matrix to be matched on B by rigid motion
    :param B: matrix to be matched by A
    :param centering: allow centering of A and B
    :param reflection: allow reflection of Omega
    :return Omega: rigid motion matrix Omega such that Omega*A =~ B
    """
    assert A.shape == B.shape, "arrays A and B must be of equal shape"

    if centering:
        # centering
        a = mean(A, axis=1)
        b = mean(B, axis=1)

        A_svd = (A.transpose() - a).transpose()
        B_svd = (B.transpose() - b).transpose()

    else:
        A_svd = A
        B_svd = B

    # perform SVD
    U, _, Vh = svd(matmul(B_svd, A_svd.transpose()))

    # make sure rigid motion (no reflection):
    if not reflection:
        if det(Vh) < 0.: Vh[0] = -Vh[0]

    # compute Omega
    Omega = matmul(U, Vh)

    return Omega

