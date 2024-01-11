# 排序
def data_sort(data_list, positive_sequence = True):
    for i in range(len(data_list)):
        for k in range(i + 1, len(data_list)):
            if positive_sequence:
                if data_list[i] > data_list[k]:
                    #temp = data_list[i]
                    #data_list[i] = data_list[k]
                    #data_list[k] = temp
                    data_list[i], data_list[k] = data_list[k], data_list[i]
            else:
                if data_list[i] < data_list[k]:
                    #temp = data_list[i]
                    #data_list[i] = data_list[k]
                    #data_list[k] = temp
                    data_list[i], data_list[k] = data_list[k], data_list[i]
    print(data_list)
    return [data_list]
data = [0, 6, 1, 2, 4, 5, 3]
data_sort(data, positive_sequence = False)