import pathlib
with open(pathlib.Path("D:/project/object/test_file/new_test1.txt"), 'r', encoding='utf-8')as f:
    data_txt = f.read()

encode_data = data_txt.encode('utf-8')
print('编码完成,', encode_data)

decode_data = encode_data.decode('utf-8')
print('解码完成,', decode_data)
