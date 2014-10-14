from PIL import Image
from subprocess import Popen, PIPE, call
from imageprocessing import find_region, new_image, bounding_box

def partition_training():
    for dig in xrange(10):
        call(["rm", "-Rf", "./trainingnums/" + str(dig) + "/"])
        call(["mkdir", "./trainingnums/" + str(dig) + "/"])
        img = Image.open("./trg" + str(dig) + ".bmp", 'r')
        img.convert('L')
        pixels = img.load()

        threshold = 200

        img2 = img.point(lambda x: 0 if x < threshold else 255)

        pixels = img2.load()

        visited = set()
        digits = []

        for i in xrange(img2.size[0]):
            for j in xrange(img2.size[1]):
                if pixels[i,j] == 255:
                    visited.add((i,j))
                elif (i,j) not in visited:
                    visited, pixels, digits = find_region(i, j, \
                                                          img2.size[0], \
                                                          img2.size[1], \
                                                          visited, \
                                                          pixels, \
                                                          digits, \
                                                          0, \
                                                          2)
                else:
                    continue
        k = 0
        for digit in digits:
            minx, miny, maxx, maxy = bounding_box(digit)
            digit_img = new_image(minx, miny, maxx, maxy)
            if digit_img.size[0] > 0 and digit_img.size[1] > 0:    
                for pixel in digit:
                    digit_img.putpixel((pixel[0] - minx, pixel[1] - miny), 0)
                
                digit_img.save("./trainingnums/" + str(dig) + "/" + str(k) + ".bmp")
                k += 1

def partition_test():
    for dig in xrange(10):
        call(["rm", "-Rf", "./testnums/" + str(dig) + "/"])
        call(["mkdir", "./testnums/" + str(dig) + "/"])
        img = Image.open("./test" + str(dig) + ".bmp", 'r')
        img.convert('L')
        pixels = img.load()

        threshold = 200

        img2 = img.point(lambda x: 0 if x < threshold else 255)

        pixels = img2.load()

        visited = set()
        digits = []

        for i in xrange(img2.size[0]):
            for j in xrange(img2.size[1]):
                if pixels[i,j] == 255:
                    visited.add((i,j))
                elif (i,j) not in visited:
                    visited, pixels, digits = find_region(i, j, \
                                                          img2.size[0], \
                                                          img2.size[1], \
                                                          visited, \
                                                          pixels, \
                                                          digits, \
                                                          0, \
                                                          2)
                else:
                    continue
        k = 0
        for digit in digits:
            minx, miny, maxx, maxy = bounding_box(digit)
            digit_img = new_image(minx, miny, maxx, maxy)
            if digit_img.size[0] > 0 and digit_img.size[1] > 0:    
                for pixel in digit:
                    digit_img.putpixel((pixel[0] - minx, pixel[1] - miny), 0)
                
                digit_img.save("./testnums/" + str(dig) + "/" + str(k) + ".bmp")
                k += 1




if __name__ == '__main__':
    partition_test()
    partition_training()
