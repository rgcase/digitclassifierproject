from PIL import Image
from subprocess import Popen, PIPE, call
from imageprocessing import find_region, new_image, bounding_box
import readdata
import algorithms
import sys

def linear_regression():
    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    algorithms.linear(testcases, trainingset)

def support_vector_machine():
    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    algorithms.support_vector_machine(testcases, trainingset)

def naive_bayes():
    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    algorithms.naive_bayes(testcases, trainingset)

def rnd_for():
    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    algorithms.random_forest(testcases, trainingset)

def k_nearest_neighbour(k):

    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    correct = 0
    total_per_digit = [0] * 10
    correct_per_digit = [0] * 10

    errors = open('./errors.txt', 'w')
    
    for test in testcases:
        total_per_digit[int(test[0])] += 1
        classification = algorithms.k_nearest_neighbour(k, test, trainingset)
        if classification == test[0]:
            correct_per_digit[int(test[0])] += 1
            correct += 1
        else:
            errors.write('Misclassified ' + test[0] + ' as ' + classification + '\n')

    print 'The overall recognition rate is: ' + str(correct / float(len(testcases)))
    print 'Broken down by digit:'
    for i, num in enumerate(correct_per_digit):
        print 'For digit ' + str(i) + ': ' + str(num / float(total_per_digit[i]))


if __name__ == '__main__':
    if len(sys.argv) == 1 and sys.argv[1] == "-rndfor":
        rnd_for()
    elif len(sys.argv) == 1 and sys.argv[1] == "-bayes":
        naive_bayes()
    elif len(sys.argv) == 1 and sys.argv[1] == "-svm":
        support_vector_machine()
    elif len(sys.argv) >= 1 and sys.argv[1] == "-knn":
        try:
            k = sys.argv[2]
            k = int(k)
        except IndexError:
            k = 1
        k_nearest_neighbour(k)
    else:
        print \
        """
        Choose a classifier by adding the corresponding flag:
            Random Forest:          -rndfor
            Naive Bayes:            -bayes
            Support Vector Machine: -svm
            k-Nearest-Neighbour:    -knn

        Use the command:
            python classifier.py {classifier flag} {k (for k-Nearest-Neighbour only)}
        """


