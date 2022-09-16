'''
----问答----
0. 请问下面代码有没有毛病，为什么？
input = "I love FishC.com"
print(input)
I love FishC.com
答：有毛病, 因为input是一个内置函数, 不适合作变量名使用, 如果作为了变量名使用, 那么input()就无法使用了

1. 请问下面代码为什么会出错，应该如何解决？
print("C:\Users\goodb\Desktop")
yntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated 
\UXXXXXXXX escape
答: 因为 反斜杠加一个字母或者符号是代表着转义的意思, 而代码读到\U的时候python发现\U不是可转义的符号,所以报错













'''