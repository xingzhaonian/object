import jsonlines, json, yaml, pandas

def load_yaml(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data 
    
def load_json(file):
    json_data = []
    with jsonlines.open(file) as file:
        for i in file:
            json_data.append(i)
    return json_data

def load_excel(file):
    sheet_data = pandas.read_excel(file, engine='openpyxl', sheet_name=None)
    for i in sheet_data:
        data = pandas.read_excel(file, engine='openpyxl', sheet_name=i)

load_excel('D:\\project\\config\\table\\activity_main.xlsm')