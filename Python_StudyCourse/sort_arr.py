def sort_1(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

#print(sort_1([6,3,9,1,3,35,8,2]))




def sort_2(list):
    isswapped = True
    num = len(list)
    while isswapped:
        isswapped = False
        for i in range(num - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                isswapped = True

    return list

print(sort_2([6,3,9,1,3,35,8,2]))


