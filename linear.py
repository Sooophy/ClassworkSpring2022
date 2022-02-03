def find_y(tuple1, tuple2, x):
    x1, y1 = tuple1.split(',')
    x2, y2 = tuple2.split(',')
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    x = float(x)
    k = (y2 - y1) / (x2 - x1)
    y = k * (x-x1) + y1
    return y


def input_data(instruction):
    a = input(instruction)
    return a


def output_data(y):
    print("y = ", y)


if __name__ == "__main__":
    tuple1 = input_data("Please enter tuple1 as x, y: ")
    tuple2 = input_data("Please enter tuple2 as x, y: ")
    x = input_data("Please enter x: ")
    y = find_y(tuple1, tuple2, x)
    output_data(y)
