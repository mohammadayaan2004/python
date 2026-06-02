# ============================================================
# SciPy FFT (Fast Fourier Transform) Example
# ============================================================
#
# PURPOSE OF THIS PROGRAM:
# ------------------------
# This program generates a sine wave signal and visualizes it.
# Such signals are commonly used in:
#   1. Digital Signal Processing (DSP)
#   2. Audio Processing
#   3. Communication Systems
#   4. Image Processing
#   5. Machine Learning feature extraction
#
# Before applying FFT, we first need a signal.
# This code creates a pure sine wave that can later be transformed
# from the TIME DOMAIN to the FREQUENCY DOMAIN using FFT.
#
# FFT = Fast Fourier Transform
# It is an optimized algorithm used to calculate DFT
# (Discrete Fourier Transform).
#
# Time Domain:
#   Shows how signal amplitude changes over time.
#
# Frequency Domain:
#   Shows which frequencies are present in the signal.
#
# Example:
# A musical sound may look complicated in the time domain,
# but FFT can reveal that it consists of frequencies like:
# 100 Hz, 500 Hz, 1000 Hz, etc.
#
# Interview Question:
# Q: Why do we use FFT instead of DFT directly?
# A:
#    DFT complexity  = O(N²)
#    FFT complexity  = O(N log N)
#    FFT is much faster for large datasets.
#
# ============================================================

# NumPy is used for numerical computations
import numpy as np

# Seaborn improves graph appearance.
import seaborn as sns

# pyplot is used for plotting graphs.
from matplotlib import pyplot as plt

# Apply darkgrid style to plots.
# Makes graphs easier to read.
sns.set_style("darkgrid")

# ============================================================
# SIGNAL PARAMETERS
# ============================================================

# Frequency of sine wave in Hertz (Hz)
#
# Meaning:
# A frequency of 10 Hz means the wave completes 10 full cycles every second.
#
# Q: What is Hertz?
# A: Number of cycles per second.
frequency = 10


# Sampling Rate
#
# Number of samples collected per second.
#
# Here:
# sample_rate = 100
#
# Means:
# We record 100 data points every second.
#
# Importance:
# Sampling rate must be sufficiently high
# to capture the signal accurately.
#
# Nyquist Theorem:
# Sampling Rate >= 2 × Highest Frequency
#
# Here:
# Highest Frequency = 10 Hz
# Minimum Required Sampling Rate = 20 Hz
#
# We are using 100 Hz, which is safe.

sample_rate = 100


# ============================================================
# TIME AXIS GENERATION
# ============================================================

# np.linspace(start, stop, num_points, endpoint=False)
#
# Creates evenly spaced time values.
#
# Parameters:
# start = 0 seconds
# stop = 2 seconds
# num_points → total number of values to generate between start and stop
# num_points = 2 * sample_rate
#
# Since sample_rate = 100,
# total samples = 200
#
# endpoint=False excludes the last point (2 sec)
#
# Why?
# To avoid duplicating the first point of the next cycle.
#
# Result:
# t contains:
# [0.00, 0.01, 0.02, ..., 1.99]
#
# Interview Question:
# Q: Why use endpoint=False?
# A: To prevent duplicate sample points in periodic signals.
t = np.linspace(0, 2, 2 * sample_rate, endpoint=False)


# ============================================================
# GENERATING SINE WAVE
# ============================================================

# Formula:
#
# a = sin(2πft)
#
# where:
# f = frequency
# t = time
#
# Components:
#
# np.pi
#   Mathematical constant π ≈ 3.14159
#
# 2 * np.pi
#   Converts frequency into radians.
#
# frequency * 2 * np.pi * t
#   Angular position at each time instant.
#
# np.sin(...)
#   Calculates sine value.
#
# Result:
# Creates a 10 Hz sine wave.
#
# Interview Question:
# Q: Why is 2π used?
# A: One complete cycle equals 2π radians.
a = np.sin(frequency * 2 * np.pi * t)


# ============================================================
# PLOTTING THE SIGNAL
# ============================================================

# Plot signal amplitude against time.
#
# X-axis:
#   Time (seconds)
#
# Y-axis:
#   Signal amplitude
#
# This visualization is called the
# TIME DOMAIN REPRESENTATION.
plt.plot(t, a)


# Label x-axis.
#
# Important:
# Always label axes for clarity.
plt.xlabel('Time (s)')


# Label y-axis.
plt.ylabel("Signal Amplitude")


# Display graph.
plt.show()


# ============================================================
# INTERVIEW QUESTIONS & ANSWERS
# ============================================================

# Q1: What is Fourier Transform?
#
# A:
# A mathematical technique that converts a signal
# from time domain to frequency domain.


# Q2: What is FFT?
#
# A:
# FFT (Fast Fourier Transform) is a fast algorithm
# used to compute DFT efficiently.


# Q3: What is DFT?
#
# A:
# Discrete Fourier Transform converts discrete-time
# signals into frequency components.


# Q4: Difference between DFT and FFT?
#
# A:
# DFT:
#    Mathematical transformation.
#
# FFT:
#    Efficient algorithm to compute DFT.


# Q5: What is the Time Domain?
#
# A:
# Representation of a signal with respect to time.


# Q6: What is the Frequency Domain?
#
# A:
# Representation showing frequencies present
# inside a signal.


# Q7: Why is FFT important?
#
# A:
# It helps identify hidden frequencies inside signals,
# making analysis easier.


# Q8: Applications of FFT?
#
# A:
# - Audio compression
# - Speech recognition
# - Medical ECG analysis
# - Image processing
# - Radar systems
# - Wireless communication
# - Machine Learning feature extraction


# Q9: Why do we generate a sine wave before FFT?
#
# A:
# Because a sine wave contains a known frequency.
# After FFT, we can verify whether FFT correctly
# identifies that frequency.


# Q10: What will FFT output for this signal?
#
# A:
# Since signal frequency = 10 Hz,
# FFT will show a major peak near 10 Hz.
