from PIL import Image
from subprocess import Popen, PIPE
from imageprocessing import find_region

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
        if edge == True:
            break
        for j in xrange(img.size[1]):
            if (0, j) in hole or (img.size[0]-1, j) in hole:
                edge = True
                break
        if edge == True:
            edge = False
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

