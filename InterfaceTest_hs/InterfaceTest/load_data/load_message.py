import yaml 
import json
# 加载消息数据

def load(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        #print(data)
        return data
    

#load('O:\\皇上快点_测试\\InterfaceTest\\EMPEROR_TEST\\message_config\\useItem_shuxingguo_1216.yaml')