from PIL import Image
from subprocess import Popen, PIPE, call
from imageprocessing import find_region, new_image, bounding_box
import readdata
import algorithms


def classify():

    _, trainingset = readdata.read_training_data()
    _, testcases = readdata.read_test_data()

    correct = 0

    errors = open('./errors.txt', 'w')

    for test in testcases:
        classification = algorithms.nearest_neighbour(test, trainingset)
        if classification == test[0]:
            correct += 1
        else:
            errors.write('Misclassified ' + test[0] + ' as ' + classification + '\n')

    print correct / float(len(testcases))

if __name__ == '__main__':
    classify()
