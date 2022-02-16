from sim import euclidean_dist

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def snapshot():
        pass
    
    def epsilon_neighbourhood(self, P):
        neighbourhood = []

        for PN in range(len(self.dataset)):
            if P != PN and euclidean_dist(self.dataset[PN], self.dataset[P]) <= self.epsilon:
                # In the neighbourhood
                neighbourhood.append(PN)

        return neighbourhood

    def explore_and_assign_eps_neighbourhood(self, P, cluster, assignments):
        neighbourhood = self.epsilon_neighbourhood(P)

        while neighbourhood:
            neighbour_of_P = neighbourhood.pop()

            if assignments[neighbour_of_P] != 0:
                # 
                pass

            assignments[neighbour_of_P] = cluster

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

        for P in range(len(self.dataset)):

            if assignments[P] != 0:
                # Already assigned
                continue

            if len(self.epsilon_neighbourhood(P)) >= self.min_pts:
                # Core point
                assignments = self.explore_and_assign_eps_neighbourhood(
                    P, cluster, assignments)

        return assignments
