def sequence(data, straight = True):
    for i in range(len(data)):
        for k in range(i + 1, len(data)):
            if straight:
                if data[k] > data[i]:
                    temp = data[i]
                    data[i] = data[k]
                    data[k] = temp
            else:
                if data[k] < data[i]:
                    temp = data[k]
                    data[k] = data[i]
                    data[i] = temp
    print(data)
    return data
data = [7, 4, 3, 9, 11, 440, 678, 432, 34]
sequence(data, straight = False)
                    



