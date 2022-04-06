import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


class GaussianMixture:
    def __init__(self, n_components=5) -> None:
        """
        """
        self.n_components = n_components

    def fit(self, X):
        """
        """
        raise NotImplementedError()

    def predict(self, X):
        """
        """
        return self


if __name__ == '__main__':
    # Generate some data
    X, y_true = make_blobs(n_samples=300, centers=4,
                        cluster_std=.8, random_state=0)
    X = X[:, ::-1] # flip axes for better plotting

    plt.scatter(X[:, 0], X[:, 1], s=40, cmap='viridis')
    plt.show()

    gmm = GaussianMixture(n_components=4).fit(X)
    labels = gmm.predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
    plt.show()

    probs = gmm.predict_proba(X)
    print(probs[:5].round(3))

    size = 50 * probs.max(1) ** 2  # square emphasizes differences
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=size)
    plt.show()