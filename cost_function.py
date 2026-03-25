def compute_cost(tour, distance_matrix):
#The total tour cost is calculated using the distance matrix.
    cost = 0

    for i in range(len(tour)-1):
        cost += distance_matrix[tour[i]][tour[i+1]]

    # return to start
    cost += distance_matrix[tour[-1]][tour[0]]

    return cost