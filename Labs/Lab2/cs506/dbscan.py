import matplotlib.pyplot as plt
import numpy as np
from sim import euclidean_dist


class DBC:

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def snapshot(self, P_index, assignments):
        fig, ax = plt.subpolts()
        colours = np.array([x for x in 'bgremykbgremykbgrcmykbgrcayk'])
        ax.scatter(self.dataset[:, 0], self.dataset[:, 1],
                   color=colours[assignments].tolist(), s=10, alpha=0.8)

        # Create circle around the scatters
        cir = plt.Circle(self.dataset[P_index],
                         self.epsilon, fill=False, alpha=0.8)
        ax.add_patch(cir)
        # Necessary or else the circles appear to be oval shaped
        ax.set_aspect('equal')

        fig.savefig('temp.png')
        plt.close()

    def epsilon_neighbourhood(self, P):
        """
        Search for points in the neighbourhood
        """
        neighbourhood = []

        for PN in range(len(self.dataset)):
            if P != PN and euclidean_dist(self.dataset[PN], self.dataset[P]) <= self.epsilon:
                # In the neighbourhood
                neighbourhood.append(PN)

        return neighbourhood

    def explore_and_assign_eps_neighbourhood(self, P_index, cluster, assignments):
        neighbourhood = self.epsilon_neighbourhood(P_index)

        while neighbourhood:
            neighbour_of_P = neighbourhood.pop()

            if assignments[neighbour_of_P] != 0:
                continue

            assignments[neighbour_of_P] = cluster
            self.snapshot(neighbour_of_P, assignments)

            next_neighbourhood = self.epsilon_neighbourhood(neighbour_of_P)

            if len(next_neighbourhood) >= self.min_pts:
                # This is a core point
                # Its neighbours should be explored / assigned also
                neighbourhood.extend(next_neighbourhood)

        return assignments

    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        assignments = [0] * len(self.dataset)
        cluster = 1

        for P_index in range(len(self.dataset)):
            if assignments[P_index] != 0:
                # Already assigned
                continue

            if len(self.epsilon_neighbourhood(P_index)) >= self.min_pts:
                # Core point
                assignments = self.explore_and_assign_eps_neighbourhood(
                    P_index, cluster, assignments)

        return assignments
