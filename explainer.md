# Mathematical derivation
Based on https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem.
Berlin, 08 OCT 2024

## Problem statement
The orthogonal procrustes problem asks, given two matrices $A, B \in \mathbb{R}^{m \times n}$, 
for a orthogonal matrix $\Omega$ (i.e. $ \det \Omega = \pm 1$), such that $A$ is as well superimposed on $B$ as 
possible.

This can be stated as the optimization problem

$$ \min_\Omega \| \Omega A - B \|_F $$

under the constraint

$$ \det \Omega = \pm1, $$

where $\| \cdot \|$ denotes the Frobenius norm, which treats $m \times n$-matrices as $m \cdot n$-vectors.

## Connection to Singular Value Decomposition (SVD)
It was shown by Peter Schönemann (https://doi.org/10.1007%2FBF02289451) that the solution to

$$ \min_\Omega \| \Omega - M \|_F $$

under the constraint

$$ \det \Omega = \pm1, $$

is given by

$$ \Omega = UV^\intercal,$$

where $U\Sigma V^\intercal = M$ is the SVD of $M$.

We can reformulate the equation 

$$\Omega A -B$$ 

by applying  the *pseudo-inverse* $A^{-1}$  of $A$ and yield

$$ \Omega - BA^{-1}.$$ 

Pseudo-inverses are a notion which extends invertibility of 
matrices to non-square matrices (https://en.wikipedia.org/wiki/Generalized_inverse), for which procrustes analyses are 
desirable as well.

Thus, we can phrase the optimization problem equivalently as

$$ \min_\Omega \| \Omega - BA^{-1} \|_F $$

under the constraint

$$ \det \Omega = \pm1. $$


## Numerical considerations
Perfomrance can be improved by a numerical "hack", which is mathematically a bit more elaborate. This hack is to replace the pseudo-inverse $A^{-1}$ with the 
transpose $A^\intercal$, which is numerically very cheap to compute. This leads to 

$$ \Omega AA^\intercal - BA^\intercal.$$ 

But why does this still yield the correct result? First note that AA^\intercal is a symmetric and square matrix, which 
means that it is in most cases normally invertible. Its inverse can be written in terms of pseudo-inverses

$$ (AA^\intercal)^{-1} = (A^\intercal)^{-1}A^{-1} $$

which when applied to the equation before leads to

$$ \Omega AA^\intercal(A^\intercal)^{-1}A^{-1}  - BA^\intercal (A^\intercal)^{-1}A^{-1}  = \Omega - BA^{-1},$$

meaning that both equations are equivalent.

Secondly, Note that the SVD of $AA^\intercal$, say $\mathrm{SVD}(AA^\intercal) = U \Sigma V^\intercal$, is identical
to its orthogonal diagonalization $S^\intercal D S$ where $D=\Sigma$ and $S = V^\intercal$, because $AA^\intercal$ is a 
symmetric positive-definite matrix. That implies it encodes no rotation (because $UV^\intercal = S^\intercal S = I$) and 
thus only scales, i.e. the SVD of $\Omega$ and $\Omega AA^\intercal$ only differs in singular values, which we discard.

In conclusion, under the orthogonality constraint of $\Omega$ we can state the optimization probem equivalently as

$$ \min_\Omega \| \Omega - BA^\intercal \|_F $$

under the constraint

$$ \det \Omega = \pm1. $$

## Wrap-Up
From the previous sections, we can conclude that the orthogonal procrustes problem stated above is solved by computing
1. $U, \Sigma, V^\intercal = \mathrm {SVD}(BA^\intercal)$
2. `return` $\Omega = UV^\intercal$.

## Reflection-free procrustes
In many applications, one is interested in a so-called *rigid motion* solution, which implies a reflection-free
$\Omega$. This is achieved by the *Kabsch algorithm* (https://en.wikipedia.org/wiki/Kabsch_algorithm). It extends the algorithm from the Wrap-Up a bit:
1. $U, \Sigma, V^\intercal = \mathrm {SVD}(BA^\intercal)$
2. `if` $\det(UV^\intercal=-1)$ `return` $\Omega=U \mathrm{diag}(1,1 .., 1, -1) V^\intercal$.

This means we reflect the last column of $V$, which is the least prominent of the prinicpal axes.

