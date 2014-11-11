from math import sqrt

def euclidean_distance(test_sample, training_sample):
    return sqrt( sum(
                [abs(test_sample[i] - training_sample[i]) ** 2 \
                for i in xrange(1, len(test_sample))]
                ) )

def nearest_neighbour(test, data, dist=euclidean_distance):
    distances = map(lambda x: (x[0], dist(test, x)), data)
    classification = min(distances, key = lambda x: x[1])[0]
    return classification
