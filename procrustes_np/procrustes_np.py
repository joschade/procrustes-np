from numpy import matmul, mean, array
from numpy.linalg import svd, det, norm

def orthogonal_procrustes(A: array, B: array, centering = True, reflection = False) -> array:
    """
    :param A: matrix to be matched on B by orthogonal transformation
    :param B: matrix to be matched by A
    :param centering: allow centering of A and B
    :param reflection: allow reflection by Omega
    :return Omega: rigid motion matrix Omega such that Omega*A =~ B
    :return b-a: translation to move center of A to center of B
    :return dist: the Procrustes distance ||Omega*A -B||_F (Frobenius norm)
    """

    assert len(A.shape) == 2, "arrays A and B must be 2-dimensional"
    assert A.shape == B.shape, "arrays A and B must be of equal shape"

    if centering:
        # centering
        a = mean(A, axis=1)
        b = mean(B, axis=1)

        A = (A.transpose() - a).transpose()
        B = (B.transpose() - b).transpose()

    # perform SVD on BA^T
    U, _, Vh = svd(matmul(B, A.transpose()))

    # compute Omega
    Omega = U @ Vh

    det_Omega = det(Omega)

    # make sure rigid motion (no reflection):
    if not reflection:
        if det_Omega < 0.:
            Vh[-1] = -Vh[-1]
            Omega = U @ Vh

    # Compute the Procrustes distance (Frobenius norm)
    dist = norm(Omega @ A - B, ord='fro')

    return Omega, b-a, dist

