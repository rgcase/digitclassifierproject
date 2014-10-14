from PIL import Image
from Queue import Queue

def adjacent_pixels(pixel, visited):
    for m in [-1,0,1]:
        for n in [-1,0,1]:
            if m == 0 and n == 0:
                pass
            elif (pixel[0]+m,pixel[1]+n) not in visited:
                yield (pixel[0]+m,pixel[1]+n)

def find_region(i,j,isize,jsize,visited,pixels,digits):
    to_check = Queue()
    to_check.put((i,j))
    shape = set()
    visited.add((i,j)) 
    while not to_check.empty():
        pixel = to_check.get_nowait()
        shape.add(pixel)
        
        for adj in adjacent_pixels(pixel, visited):
            if adj not in visited and \
                0 <= adj[0] and adj[0] < isize and \
                0 <= adj[1] and adj[1] < jsize and \
                pixels[adj[0],adj[1]] == 0:
                    visited.add(adj)
                    to_check.put((adj[0],adj[1]))
    
    if len(shape) > 2:
        digits.append(shape)
    return (visited, pixels, digits)
                   
def bounding_box(digit):
    minx = float("inf")
    miny = float("inf")
    maxx = float("-inf")
    maxy = float("-inf")

    for pixel in digit:
        minx = pixel[0] if pixel[0] < minx else minx
        miny = pixel[1] if pixel[1] < miny else miny
        maxx = pixel[0] if pixel[0] > maxx else maxx
        maxy = pixel[1] if pixel[1] > maxy else maxy

    return ( minx, miny, maxx, maxy )

def new_image( minx, miny, maxx, maxy ):
    """
    Takes 4 ordered pairs as arguments corresponding to the bounding box of the
    image in the order top left, top right, bottom right, bottom left.
    Returns an image of type 'L' with size equal to the bounding box.
    """
    
    return Image.new('L', (maxx - minx + 1, maxy - miny + 1), 255) 
