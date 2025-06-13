

d = {'s':5, 'd':7, 'ss':{'d':44, 't':3445, 'fsd':{'flm':99, 'lpl':{'lck':1991}}}, '张飞':909}

def arrange_dict(data):
    stack = [[data, '']]
    sep ='.'
    result = {}
    while stack:
        total_data = stack.pop()
        dict_data = total_data[0]
        key_name = total_data[1]

        for key, value in dict_data.items():
            if key_name:
                new_key_name = key_name + sep + key
            else:
                new_key_name = key
            if isinstance(value, dict):
                stack.append([value, new_key_name])
            else:
                result[new_key_name] = value
    return result







def recursion_dict_data(data, key_name =''):
    result = {}
    for key, value in data.items():
        if key_name:
            new_key_name = key_name + '.' + key
        else:
            new_key_name = key
        if isinstance(value, dict):
            each_result = recursion_dict_data(value, new_key_name)
            result.update(each_result)
        else:
            result[new_key_name] = value
    return result


#recursion_dict_data(d)
#print(result)
#print(recursion_dict_data(d))


def fanil(num):
    if num == 1:
        return num
    else:
        result = num * fanil(num-1)
        print(result)
    return result






        





item = {}
def flatten_dict_1(data, k_name= '', sep='.'):
    for k, v in data.items():
        if k_name:
            new_key = k_name + sep + k
        else:
            new_key = k
        if isinstance(v, dict):
            result = flatten_dict_1(v, new_key, sep)
            item.update(result)
        else:
            item[new_key] = v
    return item



def stack_dict(data):
    sep = '.'
    result = {}
    stack = [(data, '')]
    while stack:
        dict_data, key_name = stack.pop()
        for k, v in dict_data.items():
            if key_name:
                new_key_name = key_name + sep + k
            else:
                new_key_name = k
            if isinstance(v, dict):
                stack.append((v, new_key_name))
            else:
                result[new_key_name] = v
    return result
               

lists =[3,3,4,4, 5,7]

def find_missing_number(data):
    if not data:
        return 0
    if len(data) == 1:
        return 2
    data.sort()
    if (len(data) == 1) and (data[0] == 0):
        return 1
    for i in range(len(data)):
        if i + 1 < len(data) :
            if data[i] + 1 == data[i + 1]:
                    continue
            else:
                result = data[i] + 1
                return result
    else:
        return None




def count_letters(s):
    dic_data = {}
    if s:
        for i in s:
            lower_str = i.lower()
            if lower_str.isalpha():
                if lower_str in dic_data:
                    dic_data[lower_str] += 1
                else:
                    dic_data[lower_str] = 1
    else:
        return None
    sorted_data = sorted(dic_data.items(), key = lambda x:x[1])
    return sorted_data






str_dict = {
    "name": "Alice",
    "city": "New York",
    "job": "Engineer",
    "hobby": "Reading"
}

num_dict = {
    "age": 25,
    "height": 175.5,
    "weight": 68.2,
    "score": 95
}

mixed_dict = {
    "name": "Bob",          # str
    "age": 30,              # int
    "salary": 5000.75,      # float
    "is_student": False,    # bool (Python 里 bool 是 int 的子类)
    "address": "Beijing"    # str
}


edge_case = {
    "b": "a",  # 键 "b"，值 "a"
    "a": "b",  # 键 "a"，值 "b"
    "c": "a"   # 键 "c"，值 "a"
}

data = {"a": 2, "b": 1, "c": 2} 
                

def dict_sort(dict_items, index = 0, reverse=False):
    '''
    参数说明:
    dict_items: 该参数为dict数据类型
    index: 0表示使用dict的键进行排序, 1表示使用dict的值进行排序
    reverse: 是否反转, 默认为不反转
    '''
    if not isinstance(dict_items, dict):
        raise TypeError('需要字典类型数据')
    
    if not dict_items:
        raise ValueError('数据不能为空,需要字典类型数据')
    
    if index not in (0, 1):
        raise ValueError('index 必须是 0 (键排序) 或 1 (值排序)')

    sort_list = []
    result = []
    if index == 0:
        pos_value = 1
    if index == 1:
        pos_value = 0
    dict_list = list(dict_items.items())
    for i in dict_list:
        sort_list.append(i[index])
    if not reverse:
        sort_list.sort(key=lambda x:str(x))
    else:
        sort_list.sort(key=lambda x:str(x), reverse=True)
    for i in sort_list:
        for k in dict_list:
            if i == k[index]:
                if index == 0:
                    result.append((i, k[pos_value]))
                else:
                    result.append((k[pos_value], i))

    return dict(result)








