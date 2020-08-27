import pandas as pd
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-inputFile',
        default='iris.data',
        type=str,
        help='name of file that will be worked')
    parser.add_argument(
        '-sep',
        default=',',
        help='column identifier')
    parser.add_argument(
        '-dec',
        default='.',
        help='decimal identifier')
    parser.add_argument(
        '-distance',
        default=1,
        type=int,
        help='1 for euclidean and 2 for manhattan')
    parser.add_argument(
        '-outputFile',
        default='distances.csv',
        type=str,
        help='name of result file')

    return parser.parse_args()


def abs(x):
    if x < 0:
        return x * (-1)
    return x


def minkowski_distance(x, y, r):
    exp = 0.0
    tam = len(y) if (len(x) > len(y)) else len(x)
    for i in range(tam):
        exp += abs((x[i] - y[i])) ** r
    return exp ** (1 / r)


def euclidean_distance(x, y):
    return minkowski_distance(x, y, 2)


def manhattan_distance(x, y):
    return minkowski_distance(x, y, 1)


def all_versus_all(df, distance):
    calculated_distance = []
    for i in df.values:
        for j in df.values:
            if distance == 1:
                calculated_distance.append(euclidean_distance(i, j))
            else:
                calculated_distance.append(manhattan_distance(i, j))

    return calculated_distance


def write_file(data, file):
    with open(file, 'w') as f:
        for i in range(len(data)):
            if i == 0:
                f.write("%s" % data[i])
            else:
                f.write(",%s" % data[i])


args = get_args()
df = pd.read_csv(args.inputFile, sep=args.sep, decimal=args.dec, header=None)
write_file(all_versus_all(df, args.distance), args.outputFile)
