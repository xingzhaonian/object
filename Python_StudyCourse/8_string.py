'''
string

字符串是一个序列
字符串可以用切片的方式进行查找等
s = '12321'
s[::] 就等于 s[::-1] s是一个回文数

字符串用法大合集
1, capitalize()----------------------------------返回一个首字母大写版本的新字符串(新字符串的首字母变为大写, 其他字母变为小写)
2, casefold()------------------------------------返回一个小写版本的字符串(新字符串的所有字母变为小写)
3, center(width, fillchar='')--------------------返回一个字符居中的新字符串(width <=字符串长度, 新字符串=原字符串; width>字符串宽度, 所有字符
居中, 左右使用fillchar参数指定的字符填充)
4, count(sub,[start,[end]])----------------------返回sub字符串中不重叠的出现次数, 可选参数为start和end, 用来控制起始位置和结束位置
5, encode(encoding='utf-8', errors='strict')-----以encoding参数指定的编码格式对字符串进行编码. errors参数指定编码出现错误时的解决方案, 
默认的 strict 表示如果出错, 则抛出一个UnicodeEncodeError的异常. 其他可用的参数值是'ignore', 'replace'和'xmlcharrefreplace'
6, endswith(suffix[, start[, end]]) -------------如果字符串是以suffix指定的子字符串为结尾, 那么返回True, 否则返回False; 可选参数start
和end, 用于指定起始位置和结束位置, suffix 参数允许以元组的形势提供多个字符串
7, expandtabs([tabsize=8]) ----------------------返回一个使用空格替换制表符的新字符串, 如果没有指定tabsize参数, 那么默认一个制表符 = 8个空格

'''