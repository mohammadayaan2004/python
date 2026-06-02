# WHAT IS INTERPOLATION?
# ----------------------
# Interpolation is a technique used to estimate unknown values between known 
# data points.
#
# Example:
#
# Known:
# x = 1 → y = 10
# x = 2 → y = 20
#
# Question:
# What is y when x = 1.5 ?
#
# Interpolation estimates that value.

import numpy as np

# Import interpolation function from SciPy.
#
# interp1d =
# Interpolation in 1 dimension.
#
# Used to create a mathematical function from
# existing data points.
from scipy.interpolate import interp1d

# Matplotlib is used for plotting graphs.
#
# pyplot contains functions such as:
# plot()
# scatter()
# xlabel()
# ylabel()
# show()
import matplotlib.pyplot as plt

# ============================================================
# CREATE ORIGINAL DATA
# ============================================================

# np.linspace(start, stop, number_of_points)
#
# Creates evenly spaced values.
#
# start = 0
# stop = 5
# total points = 10
#
# Output:
# [0.0, 0.55, 1.11, ..., 5.0]
#
# Interview Question:
# Q: Why use linspace?
# A: To generate evenly spaced values.
x = np.linspace(0, 5, 10)


# Generate y values.
#
# np.cos() computes cosine values.
#
# Formula:
#
# y = cos(x²/3 + 4)

y = np.cos(x**2 / 3 + 4)

# ============================================================
# PLOT ORIGINAL DATA POINTS
# ============================================================

# scatter()
#
# Displays individual points.
#
# c='r'
#
# c = color
# r = red
#
# Other colors:
# 'b' = blue
# 'g' = green
# 'k' = black
plt.scatter(x, y, c='r')


# Show graph.
plt.show()


# ============================================================
# CREATE INTERPOLATION FUNCTIONS
# ============================================================

# interp1d(x,y)
#
# Creates a function using known data points.

# LINEAR INTERPOLATION
#
# kind='linear'
#
# Joins points using straight lines.

fun1 = interp1d(x, y, kind='linear')


# CUBIC INTERPOLATION

fun2 = interp1d(x, y, kind='cubic')

# ============================================================
# CREATE NEW X VALUES
# ============================================================

# Original data had only 10 points.
#
# Now we create 30 points.
#
# More points = smoother graph.
#
# We want interpolation to estimate
# values at these new locations.
xnew = np.linspace(0, 4, 30)

plt.plot(
    x,
    y,
    'o',
    xnew,
    fun1(xnew),
    '-',
    xnew,
    fun2(xnew),
    '--'
)

plt.legend(
    ['Original Data', 'Linear', 'Cubic'],
    loc='best'
)


# Display graph.
plt.show()


# ============================================================
# IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1: What is interpolation?
#
# A:
# Estimating unknown values between known data points.


# Q2: Why is interpolation needed?
#
# A:
# Real-world data is often incomplete.
# Interpolation helps estimate missing values.


# Q3: What does interp1d mean?
#
# A:
# One-dimensional interpolation function
# provided by SciPy.


# Q4: Difference between linear and cubic interpolation?
#
# A:
# Linear:
#   Straight-line approximation
#
# Cubic:
#   Smooth curve approximation


# Q5: Which is more accurate?
#
# A:
# Cubic interpolation generally provides
# smoother and more accurate results.


# Q8: What is the advantage of SciPy interpolation?
#
# A:
# Quickly estimates unknown values
# without manually calculating equations.


# Q9: Applications of interpolation?
#
# A:
# - Image resizing
# - Machine learning preprocessing
# - Signal processing
# - Weather prediction
# - Stock market analysis
# - Scientific simulations


# Q10: What is the difference between
# scatter() and plot()?
#
# A:
# scatter():
#    Displays points only.
#
# plot():
#    Displays connected lines.
