# This program solves a system of linear equations using
# scipy.linalg.solve().
#
# Given equations:
#
# 3x + 4y + 5z = 6
# 5x + 6y + 8z = 9
# 8x + 2y + 4z = 5
#
# Instead of solving manually using elimination,
# substitution, or matrices on paper, SciPy can solve
# them quickly and accurately.
#
# ============================================================
# WHY USE scipy.linalg ?
# ============================================================
#
# scipy.linalg is SciPy's Linear Algebra module.
#
# It is used for:
# 1. Solving systems of linear equations
# 2. Finding matrix inverse
# 3. Finding determinant
# 4. Eigenvalues and eigenvectors
# 5. Matrix decomposition (LU, QR, SVD)
# 6. Scientific computing and Machine Learning

# Interview 
# Q: What are BLAS and LAPACK?
# Answer:
# BLAS (Basic Linear Algebra Subprograms) is a library containing optimized 
# routines for basic vector and matrix operations.
# LAPACK (Linear Algebra Package) is a library built on top of BLAS that provides
# advanced linear algebra algorithms such as solving linear equations, matrix 
# decompositions, eigenvalue computations, and matrix inversion.

# Q: Why use scipy.linalg instead of numpy.linalg?
#
# A:
# scipy.linalg contains all functions available in
# numpy.linalg and also provides additional advanced
# linear algebra routines. It is optimized using BLAS
# and LAPACK libraries, making it faster for many
# scientific computations.
#
# ============================================================
# IMPORTING LIBRARIES
# ============================================================

# NumPy is used for creating and working with arrays/matrices
import numpy as np

# SciPy Linear Algebra module
from scipy import linalg

# ============================================================
# MATRIX OF COEFFICIENTS
# ============================================================
#
# Equations:
#
# 3x + 4y + 5z = 6
# 5x + 6y + 8z = 9
# 8x + 2y + 4z = 5
#
# Coefficients matrix A:
#
# [3 4 5]
# [5 6 8]
# [8 2 4]
#
# This matrix contains coefficients of x, y and z.
#

a = np.array([
    [3, 4, 5],
    [5, 6, 8],
    [8, 2, 4]
])

# ============================================================
# CONSTANT MATRIX B
# ============================================================
#
# Right side values of equations:
#
# [6]
# [9]
# [5]
#

b = np.array([
    [6],
    [9],
    [5]
])

# ============================================================
# SOLVING THE EQUATIONS
# ============================================================
#
# Mathematical form:
#
# A * X = B
#
# Where:
#
# A = coefficient matrix
# X = unknown variables [x y z]
# B = constant matrix
#
# scipy.linalg.solve(A,B)
# finds X directly.
#
# IMPORTANT:
# ----------
# A must be a square matrix
# (same number of rows and columns)
#
# Otherwise solve() will generate an error.
#

x = linalg.solve(a, b)

# ============================================================
# DISPLAY THE SOLUTION
# ============================================================
#
# Output will contain values of:
#
# x
# y
# z
#

print("Solution Matrix:")
print(x)

# ============================================================
# VERIFYING THE ANSWER
# ============================================================
#
# If solution is correct:
#
# A * X - B = 0
#
# We use matrix multiplication:
#
# a.dot(x)
#
# Then subtract original constants matrix B.
#
# Expected result:
# Very small values close to zero.
#
# Due to floating point calculations,
# values may be:
#
# 0.0000000001
# -0.0000000002
#
# These are practically zero.
#

print("\nChecking Results :- All values should be zeros")
print(a.dot(x) - b)

# ============================================================
# INTERVIEW QUESTIONS & ANSWERS
# ============================================================
#
# Q1. What is Linear Algebra?
#
# Answer:
# Linear Algebra is a branch of mathematics dealing
# with vectors, matrices, and systems of linear equations.
#
# ------------------------------------------------------------
#
# Q2. What is a matrix?
#
# Answer:
# A matrix is a rectangular arrangement of numbers
# organized in rows and columns.
#
# Example:
#
# [1 2]
# [3 4]
#
# ------------------------------------------------------------
#
# Q3. What does scipy.linalg.solve() do?
#
# Answer:
# It solves a system of linear equations represented
# in matrix form:
#
# A * X = B
#
# ------------------------------------------------------------
#
# Q4. What are inputs of solve()?
#
# Answer:
#
# solve(A, B)
#
# A -> coefficient matrix
# B -> constant matrix
#
# ------------------------------------------------------------
#
# Q5. What does solve() return?
#
# Answer:
# It returns matrix X containing values of unknowns.
#
# ------------------------------------------------------------
#
# Q6. What is the condition for solve()?
#
# Answer:
# Matrix A must be:
#
# 1. Square matrix
# 2. Non-singular (determinant ≠ 0)
#
# ------------------------------------------------------------
#
# Q8. What are BLAS and LAPACK?
#
# Answer:
#
# BLAS:
# Basic Linear Algebra Subprograms
#
# LAPACK:
# Linear Algebra Package
#
# These are highly optimized libraries used internally
# by SciPy for fast mathematical computations.
#
# ------------------------------------------------------------
#
# Q9. What is the difference between np.dot()
# and ordinary multiplication (*) ?
#
# Answer:
#
# np.dot(A,B)
# performs matrix multiplication.
#
# A * B
# performs element-wise multiplication.