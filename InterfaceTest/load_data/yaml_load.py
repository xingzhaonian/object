import yaml

# 读取参数配置
def load(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        #print(type(data), data)
        return data

#load('D:\\PythonProject\\InterfaceTest\\message_config\\user.yaml')
