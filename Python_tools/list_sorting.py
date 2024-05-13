# 排序

data = [0, 6, 1, 11, 4, 32, 5]
def data_sort(data_list, positive_sequence = True):
    for i in range(len(data_list)):
        for k in range(i + 1, len(data_list)):
            if positive_sequence:
                if data_list[i] > data_list[k]:
                    data_list[i], data_list[k] = data_list[k], data_list[i]
            else:
                if data_list[i] < data_list[k]:
                    data_list[i], data_list[k] = data_list[k], data_list[i]
    return [data_list]


def data_sort(data_list, positive_sequence=False):
    data_list.sort(reverse=not positive_sequence)
    print(data_list)
    return data_list

#data_sort(data)
