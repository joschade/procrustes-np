from numpy import matmul, mean, array
from numpy.linalg import svd, det, pinv

def orthogonal_procrustes(A: array, B: array, centering = True, reflection = False) -> array:
    """
    :param A: matrix to be matched on B by rigid motion
    :param B: matrix to be matched by A
    :param centering: allow centering of A and B
    :param reflection: allow reflection of Omega
    :return Omega: rigid motion matrix Omega such that Omega*A =~ B
    """

    assert len(A.shape) == 2, "arrays A and B must be 2-dimensional"
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
    U, _, Vh = svd(matmul(B_svd, A.transpose()))

    print(f'{det(U)=}')
    print(f'{det(Vh)=}')

    # compute Omega
    Omega = matmul(U, Vh)

    # make sure rigid motion (no reflection):
    if not reflection:
        if det(Omega) < 0.: Omega[0] = -Omega[0]

    return Omega

