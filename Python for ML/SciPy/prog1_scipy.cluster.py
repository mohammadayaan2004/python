# This code is demonstrates K-Means Clustering

# Import NumPy library for numerical operations and random data generation
import numpy as np

# Import K-Means clustering and whitening (feature scaling) functions
from scipy.cluster.vq import kmeans, whiten

# Import Matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Import Seaborn for better plot styling
import seaborn as sns

# Set plot background style
sns.set_style("darkgrid")

# -----------------------------
# STEP 1: Generate Sample Data
# -----------------------------

# Number of points to generate in each cluster
pts = 100

# Create first cluster centered around (0, 0)
# Mean = [0, 0]
# Covariance matrix controls spread and shape of cluster
a = np.random.multivariate_normal(
    [0, 0],          # Center of cluster A
    [[4, 1],         # Covariance matrix
     [1, 4]],
    size=pts         # Generate 100 points
)

# Create second cluster centered around (30, 10)
b = np.random.multivariate_normal(
    [30, 10],        # Center of cluster B
    [[10, 2],        # Covariance matrix
     [2, 1]],
    size=pts         # Generate 100 points
)

# Combine both clusters into a single dataset
# Final shape becomes (200, 2)
features = np.concatenate((a, b))


# -------------------------------------
# STEP 2: Standardize Data (Whitening)
# -------------------------------------

# Scale each feature by its standard deviation
# This prevents one feature from dominating distance calculations
whitened = whiten(features)


# --------------------------------
# STEP 3: Perform K-Means
# --------------------------------

# Find 2 clusters in the dataset
# codebook = cluster centers
# distortion = clustering error measure
codebook, distortion = kmeans(whitened, 2)


# --------------------------------
# STEP 4: Visualize Results
# --------------------------------

# Plot all data points
plt.scatter(
    whitened[:, 0],   # X coordinates (all rows, first column)
    whitened[:, 1]    # Y coordinates (all rows, second column)
)

# Plot cluster centers in red
plt.scatter(
    codebook[:, 0],   # X coordinates of cluster centers
    codebook[:, 1],   # Y coordinates of cluster centers
    c='r'             # Red color
)

# Add title to graph
plt.title("K-Means Clustering")

# Label X and Y axes
plt.xlabel("Feature 1 (Whitened)")
plt.ylabel("Feature 2 (Whitened)")

# Display the graph
plt.show()

#   What this program do :- 
#   Creates two groups of random points.
#   Combines them into one dataset.
#   Normalizes (whitens) the data.
#   Uses K-Means to find 2 clusters automatically.
#   Displays the points and marks the cluster centers in red 


# ============================================================
# K-MEANS CLUSTERING REVISION NOTES
# ============================================================

# K-Means is an UNSUPERVISED MACHINE LEARNING algorithm.
# Unsupervised means there are no labels (output classes).

# Goal:
# Divide data into K groups (clusters) such that
# points inside a cluster are similar and
# points in different clusters are dissimilar.

# Distance Metric:
# K-Means uses Euclidean Distance by default.

# Euclidean Distance Formula:
# d = √((x2-x1)^2 + (y2-y1)^2)

# K = Number of clusters to find
# In this code:
# kmeans(whitened, 2)
# means find 2 clusters.

# ------------------------------------------------------------
# K-Means Working Steps
# ------------------------------------------------------------
# 1. Select K initial centroids.
# 2. Assign each point to nearest centroid.
# 3. Recalculate centroid positions.
# 4. Repeat until centroids stop moving.
# 5. Final centroids represent cluster centers.

# ------------------------------------------------------------
# Why Whitening?
# ------------------------------------------------------------
# Features with larger values dominate distance calculations.
#
# Example:
# Age = 25
# Salary = 500000
#
# Salary would dominate Euclidean distance.
#
# Whitening scales each feature using standard deviation
# so all features contribute more equally.

# ------------------------------------------------------------
# Codebook Meaning
# ------------------------------------------------------------
# codebook contains cluster centers (centroids).
#
# Shape:
# (number_of_clusters, number_of_features)
#
# In this example:
# (2, 2)
#
# 2 clusters
# 2 features (x and y)

# ------------------------------------------------------------
# Distortion Meaning
# ------------------------------------------------------------
# distortion measures clustering error.
#
# Lower distortion = better clustering.
#
# It is the average distance of points
# from their assigned cluster centroid.

# ------------------------------------------------------------
# Dataset Shape
# ------------------------------------------------------------
# Cluster A = (100,2)
# Cluster B = (100,2)
#
# Combined dataset:
# features.shape = (200,2)

# ------------------------------------------------------------
# Covariance Matrix Meaning
# ------------------------------------------------------------
# [[4,1],
#  [1,4]]
#
# Diagonal values:
# Variance of each feature.
#
# Off-diagonal values:
# Correlation between features.

# ------------------------------------------------------------
# Important Limitation of K-Means
# ------------------------------------------------------------
# 1. Need to choose K beforehand.
# 2. Sensitive to outliers.
# 3. Assumes clusters are roughly spherical.
# 4. Different random initialization
#    can produce different results.

# ------------------------------------------------------------
# Common Interview Question
# ------------------------------------------------------------
# Difference between Classification and Clustering?
#
# Classification:
#   Supervised Learning
#   Labels available
#
# Clustering:
#   Unsupervised Learning
#   Labels not available

# ------------------------------------------------------------
# Common Interview Question
# ------------------------------------------------------------
# How to choose K?
#
# 1. Elbow Method
# 2. Silhouette Score
#
# These methods help determine
# the optimal number of clusters.

# ------------------------------------------------------------
# Important SciPy Functions Used
# ------------------------------------------------------------
# np.random.multivariate_normal()
#     Generates correlated random data.
#
# np.concatenate()
#     Combines arrays.
#
# whiten()
#     Standardizes features.
#
# kmeans()
#     Performs K-Means clustering.
#
# plt.scatter()
#     Creates scatter plot.

# ------------------------------------------------------------
# Output Interpretation
# ------------------------------------------------------------
# Blue points  -> Dataset samples
# Red points   -> Cluster centroids
#
# Centroids represent the center
# of each discovered cluster.

# ============================================================
# ONE-LINE EXAM ANSWER
# ============================================================
# This program generates two random datasets,
# standardizes them using whitening,
# applies K-Means clustering to identify two clusters,
# and visualizes the data along with cluster centroids.