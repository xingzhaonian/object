# 建立一张字符表, 用来获取调整步长后的结果, 循环 A--->Z,  z--->A
plaintext_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
input_text = input('输入要转换的文本(仅支持大小写)')
while not input_text.isalpha():
    input_text = input('输入错误,(仅支持大小写)')
move_step = int(input('输入移动的步长'))
result_text = []
index_num = 0
for i in input_text:
    if int(move_step) > len(plaintext_table):
        move_step = int(move_step) % len(plaintext_table)
    if i.isupper():
        if plaintext_table.find(i) + move_step >= len(plaintext_table):
            index_num = plaintext_table.find(i) + move_step - len(plaintext_table)
        else:
            index_num = plaintext_table.find(i) + move_step
    else:
        _ = plaintext_table.find(i) + move_step 
        if _ >= len(plaintext_table):
            index_num =  (plaintext_table.find(i) + move_step) % len(plaintext_table)
        else:
            index_num = plaintext_table.find(i) + move_step
    result_text.append(plaintext_table[index_num])
print(''.join(result_text))



# 利用ord() 和chr() 方法来获取调整步长后的结果, 大小写单独换算调整步长后的结果
input_text = input('输入要转换的文本(仅支持大小写)')
while not input_text.isalpha():
    input_text = input('输入错误,(仅支持大小写)')
move_step = int(input('输入移动的步长'))
result_text = []
A_code = ord('A')
a_code = ord('a')
pointer = 0
for i in input_text:
    if i == ' ' or i =='':
        result_text.append(i)
    else:
        if i.isupper():
            pointer = A_code
        else:
            pointer = a_code
    result_text.append(chr((ord(i) - pointer + move_step) % 26 + pointer))   # 算出调整步长后的结果, %26为了防止指针溢出
print(''.join(result_text))
