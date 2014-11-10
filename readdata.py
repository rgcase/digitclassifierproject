def read_training_data(path = './trainingdata.txt'):
    file = open(path, 'r')
    col_labels = file.readline()
    data = [line.split() for line in file.readlines()]
    data = [[row[0]] + map(float, row[1:]) for row in data]
    return (col_labels, data)


if __name__ == '__main__':
    read_training_data()
