from pathlib import Path
dict_1 = {'action':88, 'blg':{'qw':76,'kpl':{'uu': 55, 'cx':23, 'lpl':{'ig':{'ts':29, 'kh':304}}}}, 'jk': 609, 'LCK':'fk'}
list_1 = [2, 3, 11, 22, 6]

def Transform_Dict(data, base_key=''):
    result = []
    sep = '.'
    if data and isinstance(data, dict):
        for key, value in data.items():
            if base_key:
                new_key = base_key + sep + key
            else:
                new_key = key
            if isinstance(value, dict):
                sub_result = Transform_Dict(value, new_key)
                result.extend(sub_result) 
            else:
                result.append((new_key, value))
    return result

print(Transform_Dict(dict_1))


def calc_num(data_list):
    print(data_list)
    total = 1
    if not data_list and isinstance(data_list, list):
        return None
    if len(data_list) == 1:
        total *= data_list[0]
        return total
    total *= data_list[0]
    sub_result = calc_num(data_list[1:])
    total *= sub_result
    return total




def search_file(file_name, path):
    result = []
    if not file_name or not path:
        return None
    p = Path(path)
    all_file = p.iterdir()
    for each_file in all_file:
        sub_path = Path(each_file)
        if each_file.isdir():
            sub_result = search_file(each_file, sub_path)
            result.append(sub_result)
        if each_file.isfile():
            result.append(each_file)
    return result

def MultiplicationTable():
    num = 1
    while num < 10:
        for i in range(1, num + 1):
            print(i ,'x', num, '=' , i * num, end= '   ')
        print('\n')
        num += 1




#MultiplicationTable()


