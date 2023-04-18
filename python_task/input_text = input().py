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
    result_text.append(chr((ord(i) - pointer + move_step) % 26 + pointer))
print(''.join(result_text))