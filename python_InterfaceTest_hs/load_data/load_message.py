import yaml 

import jsonlines
# 加载消息数据

def load(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        #print( type(data[0]), data)
        return data
    

#load('O:\\皇上快点_测试\InterfaceTest\\message_config\\sadun_visit.yaml')




def LoadJsonData(path):
    json_data = []
    with jsonlines.open(path) as f:
        for i in f:
            json_data.append(i)
    return json_data

#LoadJsonData('O:\\皇上快点_测试\\InterfaceTest\\message_config\\test_json_data.json')
