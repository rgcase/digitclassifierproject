from math import sqrt
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import cross_val_score
from sklearn import svm, linear_model
import numpy as np

def euclidean_distance(test_sample, training_sample):
    return sqrt( sum(
                [abs(test_sample[i] - training_sample[i]) ** 2 \
                for i in xrange(1, len(test_sample))]
                ) )

def nearest_neighbour(test, data, dist=euclidean_distance):
    distances = map(lambda x: (x[0], dist(test, x)), data)
    classification = min(distances, key = lambda x: x[1])[0]
    return classification

def k_nearest_neighbour(k, test, data, dist=euclidean_distance):
    distances = map(lambda x: (x[0], dist(test, x)), data)
    distances.sort(key = lambda x: x[1])

    k_nearest = distances[:k]

    votes = [0] * 10

    for pt in k_nearest:
        votes[int(pt[0])] += 1

    classification = 0

    for i in xrange(10):
        if votes[i] > votes[classification]:
            classification = i

    return str(classification)

def random_forest(tests, data):
    training_labels = np.asarray([d[0] for d in data])
    data = map(lambda x: x[1:], data)
    rfc = RandomForestClassifier(n_estimators=100)
    rfc.fit(data, training_labels)

    unlabel_tests = map(lambda x: x[1:], tests)

    predictions = rfc.predict(unlabel_tests)

    correct = 0
    total_per_digit = [0] * 10
    correct_per_digit = [0] * 10

    for i in xrange(len(tests)):
        total_per_digit[int(tests[i][0])] += 1
        if predictions[i] == tests[i][0]:
            correct_per_digit[int(tests[i][0])] += 1
            correct += 1

    print 'The overall recognition rate is: ' + str(correct / float(len(tests)))
    print 'Broken down by digit:'
    for i, num in enumerate(correct_per_digit):
        print 'For digit ' + str(i) + ': ' + str(num / float(total_per_digit[i]))

def naive_bayes(tests, data):
    training_labels = np.asarray([d[0] for d in data])
    data = map(lambda x: x[1:], data)

    gnb = GaussianNB()

    gnb.fit(data, training_labels)

    unlabel_tests = map(lambda x: x[1:], tests)

    predictions = gnb.predict(unlabel_tests)

    correct = 0
    total_per_digit = [0] * 10
    correct_per_digit = [0] * 10

    for i in xrange(len(tests)):
        total_per_digit[int(tests[i][0])] += 1
        if predictions[i] == tests[i][0]:
            correct_per_digit[int(tests[i][0])] += 1
            correct += 1

    print 'The overall recognition rate is: ' + str(correct / float(len(tests)))
    print 'Broken down by digit:'
    for i, num in enumerate(correct_per_digit):
        print 'For digit ' + str(i) + ': ' + str(num / float(total_per_digit[i]))

def support_vector_machine(tests, data):
    training_labels = np.asarray([d[0] for d in data])
    data = map(lambda x: x[1:], data)

    clf = svm.SVC(kernel = 'linear')
    clf.fit(data, training_labels)

    unlabel_tests = map(lambda x: x[1:], tests)

    predictions = clf.predict(unlabel_tests)

    correct = 0
    total_per_digit = [0] * 10
    correct_per_digit = [0] * 10

    for i in xrange(len(tests)):
        total_per_digit[int(tests[i][0])] += 1
        if predictions[i] == tests[i][0]:
            correct_per_digit[int(tests[i][0])] += 1
            correct += 1

    print 'The overall recognition rate is: ' + str(correct / float(len(tests)))
    print 'Broken down by digit:'
    for i, num in enumerate(correct_per_digit):
        print 'For digit ' + str(i) + ': ' + str(num / float(total_per_digit[i]))
