import numpy as np


class CustomKMeans:
    def __init__(self, k, max_iter=300, tol=0.001):
        self.k = k # Number of clusters
        self.max_iter = max_iter # Maximum number of iterations for KMeans
        self.tol = tol # Tolerance level to stop iterations
        self.centroids = None # Used to store centroids
        self.labels = None # Used to store the cluster assignments

    #Fits the KMeans model to the data
    def fit(self, df):
        self.dataframe = df.to_numpy()
        n_samples, n_features = self.dataframe.shape

        # Randomly assign 'k' number of centroids from the data points
        self.centroids = self.dataframe[np.random.choice(n_samples, self.k, replace=False)]

        # Iterate for 'max_iter' number of times
        for i in range(self.max_iter):
            # Assigns each data point to the nearest centroid
            self.labels = self._euclidean(self.dataframe)
            # Calculate new centroids based on the current assignment clusters
            new_centroids = self._calc_Centroids(self.dataframe)
            # Check if the centroids have moved less than the tolerance value
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break
            self.centroids = new_centroids

    # Predicts the cluster of each data point in a dataframe
    def predict(self, df):
        # Convert dataframe to NumPy array
        dataframe = df.to_numpy()
        if self.centroids is None:
            raise ValueError("Model has not been fitted yet")
        # Assigns the new points to the closest centroid
        return self._euclidean(dataframe)

    # Method that returns the dissimilarity or Sum of Squared Errors for the clustering solution
    def sse(self):
        if self.labels is None or self.centroids is None:
            raise ValueError("Model has not been fitted yet")
        sse = 0
        # Iterate over each cluster and its centroid
        for i, centroid in enumerate(self.centroids):
            cluster_points = np.where(self.labels == i)[0]
            # Compute the squared differences between points and the centroid and get their sum
            sse += np.sum(np.square(self.dataframe[cluster_points] - centroid))

        return sse

    # Helper method to assign each data point to the nearest centroid based on Euclidean distance
    def _euclidean(self, df):
        #Calculates the Euclidean distance from each point to the centroid
        distances = np.array([np.linalg.norm(df - centroid, axis=1) for centroid in self.centroids])
        #Assigns each data point to the nearest centroid
        return np.argmin(distances, axis=0)

    # Helper method to calculate the new centroids as the mean of points assigned to each cluster
    def _calc_Centroids(self, df):
        # Initialize an array to store the new centroids
        centroids = np.zeros((self.k, df.shape[1]))
        # Iterate over each cluster
        for j in range(self.k):
            # Accumulate all the points that are assigned to the cluster
            cluster_points = df[self.labels == j]
            # If there are points in the cluster, calculate their mean to create the new centroid
            if len(cluster_points) > 0:
                centroids[j] = cluster_points.mean(axis=0)
        return centroids
