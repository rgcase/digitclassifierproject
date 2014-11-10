from math import sqrt

def euclidean_distance(test_sample, training_sample):
    return sqrt( sum(
                [abs(test_sample[i-1] - training_sample[i]) ** 2 \
                for i in xrange(1, len(test_sample))]
                ) )

def nearest_neighbour(test, data, dist):
    distances = map(lambda x: (x[0], euclidean_distance(test, x)), data)
    classification = min(distances, key = lambda x: x[1])[0]
    return classification
