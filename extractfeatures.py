from PIL import Image
from subprocess import Popen, PIPE
from imageprocessing import find_region
import csv
from sys import argv

def blackness_ratio(img):
    total = float(img.size[0] * img.size[1])
    pixels = img.load()
    count = 0


    for i in xrange(img.size[0]):
        for j in xrange(img.size[1]):
            if pixels[i,j] == 0:
                count += 1

    return count / total

def aspect_ratio(img):
    return (img.size[0] + 1) / float(img.size[1] + 1)


def number_of_holes(img):
    visited = set()
    holes = []
    pixels = img.load()

    for i in xrange(img.size[0]):
        for j in xrange(img.size[1]):
            if pixels[i,j] == 0:
                visited.add((i,j))
            elif (i,j) not in visited:
                visited, pixels, holes = find_region(i, j, \
                                                     img.size[0], \
                                                     img.size[1], \
                                                     visited, \
                                                     pixels, \
                                                     holes, \
                                                     255, \
                                                     0)
            else:
                continue
    holes_on_edges = 0
    for hole in holes:
        edge = False
        for i in xrange(img.size[0]):
            if (i, 0) in hole or (i, img.size[1]-1) in hole:
                edge = True
                break
        else:
            for j in xrange(img.size[1]):
                if (0, j) in hole or (img.size[0]-1, j) in hole:
                    edge = True
                    break
        if edge == True:
            holes_on_edges += 1
    return len(holes) - holes_on_edges

def half_blackness_ratio(img, half):
    """
    Takes an image and half identifier, one of 'top', 'bottom', 'left', 'right'.
    Return the blackness ratio of the given half of the image.
    """
    if half == "top" or half == "bottom":
        mid = img.size[1] / 2
        newimg = img.crop((0,0,img.size[0],mid)) if half == "top" else \
                 img.crop((0,mid,img.size[0],img.size[1]))
    elif half == "left" or half == "right":
        mid = img.size[0] / 2
        newimg = img.crop((0,0,mid,img.size[1])) if half == "left" else \
                 img.crop((mid,0,img.size[0],img.size[1]))
    else:
        print "half_blackness_ratio called with invalid half parameter"


    return blackness_ratio(newimg)

def horizontal_line_ratio(img):
    in_black = False
    pixels = img.load()
    max_line = 0
    for j in xrange(img.size[1]):
        count = 0
        for i in xrange(img.size[0]):
            if pixels[i,j] == 0:
                count += 1
                in_black = True
            elif in_black:
                max_line = count if max_line < count else max_line
                count = 0
                in_black = False
        else:
            max_line = count if max_line < count else max_line
            count = 0
    return max_line / float(img.size[0])

def vertical_line_ratio(img):
    in_black = False
    pixels = img.load()
    max_line = 0
    for i in xrange(img.size[0]):
        count = 0
        for j in xrange(img.size[1]):
            if pixels[i,j] == 0:
                count += 1
                in_black = True
            elif in_black:
                max_line = count if max_line < count else max_line
                count = 0
                in_black = False
        else:
            max_line = count if max_line < count else max_line
            count = 0
    return max_line / float(img.size[1])



def writedata(datawriter, i, opt):

    result = Popen(['ls', './' + opt + 'nums/' + str(i) + '/'], stdout=PIPE).communicate()
    result = result[0].splitlines()

    for file in result:
        if file:
            img = Image.open('./' + opt + 'nums/' + str(i) + '/' + file, 'r')
            if img.size[0] != 0 and img.size[1] != 0 and \
               img.size[0] != 1 and img.size[1] != 1:
                datawriter.writerow([str(i), \
                                 str(blackness_ratio(img)), \
                                 str(aspect_ratio(img)), \
                                 str(number_of_holes(img)), \
                                 str(half_blackness_ratio(img, "top")), \
                                 str(half_blackness_ratio(img, "bottom")), \
                                 str(half_blackness_ratio(img, "left")), \
                                 str(half_blackness_ratio(img, "right")), \
                                 str(horizontal_line_ratio(img)), \
                                 str(vertical_line_ratio(img)), \
                                 ])
                img.close()


def write_training_data():
    csvfile = open('trainingdata.txt', 'wb')
    datawriter = csv.writer(csvfile, delimiter = ' ')

    datawriter.writerow(['digit', \
                     'blackness_ratio', \
                     'aspect_ratio', \
                     'number_of_holes', \
                     'top_blackness_ratio', \
                     'bottom_blackness_ratio', \
                     'left_blackness_ratio', \
                     'right_blackness_ratio', \
                     'horizontal_line_ratio', \
                     'vertical_line_ratio', \
                     ])

    for i in xrange(10):
        writedata(datawriter, i, 'training')

def write_test_data():
    csvfile = open('./testdata.txt', 'wb')
    datawriter = csv.writer(csvfile, delimiter = ' ')

    datawriter.writerow(['digit', \
                         'blackness_ratio', \
                         'aspect_ratio', \
                         'number_of_holes', \
                         'top_blackness_ratio', \
                         'bottom_blackness_ratio', \
                         'left_blackness_ratio', \
                         'right_blackness_ratio', \
                         'horizontal_line_ratio', \
                         'vertical_line_ratio', \
                         ])

    for i in xrange(10):
        writedata(datawriter, i, 'test')



if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == '-train':
        write_training_data()
    elif len(argv) > 1 and argv[1] == '-test':
        write_test_data()
    else:
        write_training_data()
        write_test_data()
