
writefile = open('./featureanalysis.txt', 'w')

readfile = open('./trainingdata.txt', 'r')
data = readfile.readlines()

data = [line.split() for line in data[1:]]

data = [[row[0]] + map(lambda x: round(float(x), 1), row[1:3]) + \
        [row[3]] + map(lambda x: round(float(x), 1), row[4:]) for \
        row in data]

j = 0

for i in xrange(10):
    digit = str(i)
    count = 0

    black_ratio = {}
    aspect_ratio = {}
    holes = {}
    top_black = {}
    bottom_black = {}
    left_black = {}
    right_black = {}
    horiz_line = {}
    vert_line = {}

    while j < len(data) and data[j][0] == digit:
        black_ratio[data[j][1]] = black_ratio.get(data[j][1], 0) + 1
        aspect_ratio[data[j][2]] = aspect_ratio.get(data[j][2], 0) + 1
        holes[data[j][3]] = holes.get(data[j][3], 0) + 1
        top_black[data[j][4]] = top_black.get(data[j][4], 0) + 1
        bottom_black[data[j][5]] = bottom_black.get(data[j][5], 0) + 1
        left_black[data[j][6]] = left_black.get(data[j][6], 0) + 1
        right_black[data[j][7]] = right_black.get(data[j][7], 0) + 1
        horiz_line[data[j][8]] = horiz_line.get(data[j][8], 0) + 1
        vert_line[data[j][9]] = vert_line.get(data[j][9], 0) + 1

        j += 1
        count += 1

    count = float(count)

    writefile.write('Digit ' + digit + ' feature values:\n')
    writefile.write('Blackness Ratio\n')
    for key in black_ratio:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (black_ratio[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Aspect Ratio\n')
    for key in aspect_ratio:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (aspect_ratio[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Number of Holes\n')
    for key in holes:
        writefile.write('\t' + key + '\t' + \
                str( int( 100 * (holes[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Top Blackness Ratio\n')
    for key in top_black:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (top_black[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Bottom Blackness Ratio\n')
    for key in bottom_black:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (bottom_black[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Left Blackness Ratio\n')
    for key in left_black:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (left_black[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Right Blackness Ratio\n')
    for key in right_black:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (right_black[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Horizontal Line Ratio\n')
    for key in horiz_line:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (horiz_line[key] / count))) + '\n')
    writefile.write('\n')

    writefile.write('Vertical Line Ratio\n')
    for key in vert_line:
        writefile.write('\t' + str(key) + '\t' + \
                str( int( 100 * (vert_line[key] / count))) + '\n')
    writefile.write('\n')












