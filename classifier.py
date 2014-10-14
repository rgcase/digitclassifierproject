from PIL import Image
from subprocess import Popen, PIPE, call
from imageprocessing import find_region, new_image, bounding_box



if __name__ == '__main__':
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
                                                          digits)
                else:
                    continue
        k = 0
        for digit in digits:
            #print digit
            minx, miny, maxx, maxy = bounding_box(digit)
            #print minx, miny, maxx, maxy
            digit_img = new_image(minx, miny, maxx, maxy)
            for pixel in digit:
                digit_img.putpixel((pixel[0] - minx, pixel[1] - miny), 0)
            
            digit_img.save("./trainingnums/" + str(dig) + "/" + str(k) + ".bmp")
            k += 1


        


        


