# ============================================================
# SCIPY CONSTANTS MODULE
# ============================================================
# scipy.constants contains:
# 1. Mathematical constants (pi, golden, etc.)
# 2. Physical constants (Boltzmann constant, speed of light, etc.)
# 3. Unit conversion factors
#
# Useful when scientific values need high precision and
# should not be hardcoded manually.
# ============================================================

import scipy

# Golden Ratio (φ) = (1 + √5) / 2
# Commonly appears in mathematics, geometry, nature, and art.
# scipy.constants.golden returns a predefined high-precision value.
print("SciPy Golden Ratio Value = %0.50f" % scipy.constants.golden)

from scipy.constants import find

# find(keyword)
# Searches all available constant names containing the keyword.
# Useful when you know part of a constant name but not the exact name.
#
# Example:
# find('electron')
# find('light')
# find('boltzman')
print("\nConstants containing 'boltzman':")
print(find('boltzman'))

# physical_constants is a DICTIONARY
#
# Structure:
# {
#   constant_name :
#       (value, unit, uncertainty)
# }
#
# Key   -> constant name (string)
# Value -> tuple(value, unit, uncertainty)
#
# To see all available constants:
# print(scipy.constants.physical_constants.keys())

boltzmann_hz = scipy.constants.physical_constants['Boltzmann constant in Hz/K']

# Returned object type:
# tuple
#
# Format:
# (value, unit, uncertainty)
#
# Example:
# (20836619120.0, 'Hz K^-1', 0.0)

print("\nBoltzmann constant in Hz/K:")
print("Value =", boltzmann_hz[0])
print("Unit =", boltzmann_hz[1])
print("Uncertainty =", boltzmann_hz[2])

# ------------------------------------------------------------
# Index Meaning
# ------------------------------------------------------------
# boltzmann_hz[0] -> Numerical value
# boltzmann_hz[1] -> Unit
# boltzmann_hz[2] -> Uncertainty
# ------------------------------------------------------------

# Better Pythonic way:
# value, unit, uncertainty = boltzmann_hz

# Why tuple?
# Physical constants always have fixed information:
# 1. Value
# 2. Unit
# 3. Uncertainty
#
# Since these values should not change,
# SciPy stores them in an immutable tuple.

# Interview / Viva Point:
# physical_constants -> Dictionary
# Each dictionary value -> Tuple
#
# Dictionary Access:
# physical_constants['Boltzmann constant in Hz/K']
#
# Tuple Access:
# boltzmann_hz[0]

# Useful constants to remember:
# scipy.constants.pi        -> π
# scipy.constants.golden    -> Golden Ratio
# scipy.constants.c         -> Speed of Light
# scipy.constants.G         -> Gravitational Constant
# scipy.constants.h         -> Planck Constant
# scipy.constants.k         -> Boltzmann Constant
# scipy.constants.e         -> Elementary Charge