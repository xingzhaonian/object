>>> # 字符串拼接速度大比拼 #
>>> # test1 是加号（+）拼接法
>>> def test1(n):
        result = ""
        for i in range(n):
                result += "FishC"
        return result

>>> # test2 是使用字符串的join()方法进行拼接
>>> def test2(n):
        str_list = []
        for i in range(n):
                str_list.append("FishC")
        return "".join(str_list)

>>> # 测试开始 #
>>> # timeit模块是用于计时滴，咱以后会讲到^o^
>>> import timeit
>>> 
>>> # 第一轮：1万个 "FishC" 拼接 #
>>> timeit.timeit("test1(10000)", setup="from __main__ import test1", number=1)
0.0012263000000984903
>>> timeit.timeit("test2(10000)", setup="from __main__ import test2", number=1)
0.0009582000000136759
>>> 
>>> # 第二轮：10万个 "FishC" 拼接 #
>>> timeit.timeit("test1(100000)", setup="from __main__ import test1", number=1)
0.011719300000095245
>>> timeit.timeit("test2(100000)", setup="from __main__ import test2", number=1)
0.006204399999887755
>>> 
>>> # 第三轮：100万个 "FishC" 拼接 #
>>> timeit.timeit("test1(1000000)", setup="from __main__ import test1", number=1)
1.2601186999997935
>>> timeit.timeit("test2(1000000)", setup="from __main__ import test2", number=1)
0.08013690000007045
>>> 
>>> # 第四轮：1000万个 "FishC" 拼接 #
>>> timeit.timeit("test1(10000000)", setup="from __main__ import test1", number=1)
131.86178619999987
>>> timeit.timeit("test2(10000000)", setup="from __main__ import test2", number=1)
0.8771347999995669
>>> 
>>> # 第五轮：1亿个 "FishC" 拼接 #
>>> timeit.timeit("test1(100000000)", setup="from __main__ import test1", number=1)
13738.4885822
>>> timeit.timeit("test2(100000000)", setup="from __main__ import test2", number=1)
8.882412499999191
