def readserie(filename):
    with open(filename, 'r') as file:
        data = [float(line.strip()) for line in file.readlines()]
    return data