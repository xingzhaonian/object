text = 'ilovefishccccccdwdagaaaaaaFFiiiisshCjCCCCC'
result_list = []
for i in text:
    if text.count(i) >= 3:
        if i in result_list:
            continue
        else:
            result_list.append(str(i))
            result_list.append(str(text.count(i)))
    else:
        result_list.append(str(i))
result_txt = ''.join(result_list)
text_num = len(text)
result_txt_num = len(result_txt)
print(f'压缩前为:{text};  压缩后为:{result_txt},   压缩率为:{result_txt_num / text_num * 100:.2f} %')