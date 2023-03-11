'''
问答题

0. 用 f-string, 最需要注意的是什么?
答: 需要注意的是当前版本是否支持该语法

1. 请问下面代码会打印什么内容？
f"{{1 + 2}}"
答: 会打印 {1 + 2}

2. 请问下面代码会打印什么内容？
f"{{{1 + 2}}}"
答: 会打印 {3}

3. 请将下面 format() 格式化字符串修改为 f-string 的格式？
"{:.{prec}f}".format(3.1415, prec=2)
答: 
prec = 2
f'{3.1415:.{prec}f}'

4. 请问下面代码会打印什么内容？
f"{520:.2}"
答: 会报错, 因为.2是截取的意思, 但是参数 520 不可被截取, 如果是浮点数或者字符串就行了

5. 请将下面 format() 格式化字符串修改为 f-string 的格式？

"{:{fill}{align}{width}.{prec}{ty}}".format(3.1415, fill='$', align='^', width=10, prec=2, ty='f')
答:
prec=2
ty='f'
fill = '$'
align='^'
width=10
f'{3.1415:{fill}{align}{width}.{prec}{ty}}'
'''


"""
动动手：
0. 相信大家对于压缩和解压缩的操作并不陌生，但对其内部的实现原理，你又知道多少呢？
接下来请大家跟着题目的提示，一起来实现字符串的压缩和解压缩吧
利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。比如，字符串 FFiiiisshCCCCCC 压缩后变成 F2i4s2h1C6(15字符 -> 10字符, 66% 压缩率）
这种朴素的压缩算法并不总是理想的，比如 FFishCC 压缩后反而变长了 F2i1s1h1C2, 这可就不是我们想要的了, 所以对于重复次数小于 3 的字符，我们的程序应该选择不对其进行压缩
"""
# 压缩
compress_text = 'iiiiiilovefssshccccccdwdaaaaaaagFFhCCCCCCj'
compress_result_list = []
for i in compress_text:
    if compress_text.count(i) >= 3:
        if i in compress_result_list:
            continue
        else:
            compress_result_list.append(str(i))
            compress_result_list.append(str(compress_text.count(i)))
    else:
        compress_result_list.append(str(i))
compress_result_txt = ''.join(compress_result_list)
text_num = len(compress_text)
result_txt_num = len(compress_result_txt)
print(f'压缩前为:{compress_text};  压缩后为:{compress_result_txt},   压缩率为:{result_txt_num / text_num * 100:.2f} %')


# 1. 请大家编写一个解压程序，将上一题压缩后的字符串进行解压缩。
# 解压缩
decompression_text = 'i6lovefs3hc6dwda7gFFhC6j'
decompression_result_list = []
index_count = 0
for i in decompression_text:
    if i.isdecimal():
        for k in range(int(i) - 1):
            x = decompression_text.index(i, index_count - 1 , len(decompression_text)) - 1
            y = decompression_text.index(i, index_count - 1 , len(decompression_text))
            index_text = decompression_text[decompression_text.index(i, index_count - 1 , len(decompression_text)) - 1 :\
                                             decompression_text.index(i, index_count - 1 , len(decompression_text))]
            decompression_result_list.append(index_text)
    else:
        decompression_result_list.append(i)
    index_count += 1
decompression_result_text = ''.join(decompression_result_list)
print(f'压缩后为{decompression_text}, 解压缩后为{decompression_result_text}')