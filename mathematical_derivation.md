# Mathematical derivation
Based on https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem.

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
matrices to non-square matrices (https://en.wikipedia.org/wiki/Generalized_inverse), for which procrustes analyses are desirable as well.

## Wrap-Up
From the previous sections, we can conclude that the orthogonal procrustes problem stated above is solved by computing
1. $U, \Sigma, V^\intercal = \mathrm {SVD}(BA^{-1})$
2. `return` $\Omega = UV^\intercal$

## Reflection-free procrustes
In many applications, one is interested in a so called *rigid motion* solution, which implies a reflection-free
$\Omega$.

In this implementation, we achieve this by making sure that $\det V=1$ by reflecting the first column of $V$ if necessary.
