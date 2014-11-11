from PIL import Image
from subprocess import Popen, PIPE, call
from imageprocessing import find_region, new_image, bounding_box
import readdata
import algorithms

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

def k_nearest_neighbour():

    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    correct = 0

    errors = open('./errors.txt', 'w')

    for test in testcases:
        classification = algorithms.k_nearest_neighbour(1, test, trainingset)
        if classification == test[0]:
            correct += 1
        else:
            errors.write('Misclassified ' + test[0] + ' as ' + classification + '\n')

    print correct / float(len(testcases))

if __name__ == '__main__':
    #k_nearest_neighbour()
    rnd_for()
    #naive_bayes()
    #support_vector_machine()
