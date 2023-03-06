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
print(f'压缩后为{decompression_text} ,解压缩后为{decompression_result_text}')