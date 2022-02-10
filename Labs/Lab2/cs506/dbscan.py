class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def epsilon_neighbourhood(P):
        return []

    def explore_and_assign_eps_neighbourhood(P, cluster, assignments):
        # TODO implement
        return assignments

    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        assignments = [0] * len(self.dataset)
        cluster = 1

        for P in range(len(self.dataset)):

            if assignments[P] != 0:
                # Already assigned
                continue

            if len(self.epsilon_neighbourhood(P)) >= self.min_pts:
                # Core point
                assignments = self.explore_and_assign_eps_neighbourhood(
                    P, cluster, assignments)

        return assignments
