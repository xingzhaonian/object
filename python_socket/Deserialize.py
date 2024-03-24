'''
GetBytes    --int (1个字节)
GetBool     --bool (1个字节)
GetShort    --int (2个字节)
GetInt      --int (4个字节)
GetLong     --int (8个字节)
GetString   --str (调用Getint取出长度, 再将str.)
Getfloat    --float (struct.unpack,   4个字节)
GetDouble   --int (8个字节)
'''

import struct
class Analysis(object):

    # 初始化指针, 跟踪当前位置
    def __init__(self, bytes_data):
        self.index = 0
        self.bytes_data = bytes_data

    # 获取 1 个字节的Int
    def GetBytes(self):
        self.bytes = self.bytes_data[self.index:self.index+1]
        self.bytes = int.from_bytes(self.bytes, byteorder='little')
        self.index += 1
        print(f'指针位置{self.index}')
        return self.bytes

    # 获取 1 个字节的bool, 0 or 1
    def GetBool(self):
        self.bool_bytes = self.bytes_data[self.index:self.index+1]
        self.bool_bytes = int.from_bytes(self.bool_bytes, byteorder='little')
        self.index += 1
        print(f'指针位置{self.index}')
        return self.bool_bytes
    
    # 获取 2 个字节的int
    def GetShort(self):
        self.short = self.bytes_data[self.index:self.index + 2]
        self.short = int.from_bytes(self.short, byteorder='little')
        self.index += 2
        print(f'指针位置{self.index}')
        return self.short

    # 获取 4 个字节的int
    def GetInt(self):
        self.ints = self.bytes_data[self.index:self.index+4]
        self.ints = int.from_bytes(self.ints, byteorder='little')
        self.index += 4
        print(f'指针位置{self.index}')
        return self.ints

    # 获取 8 个字节的int
    def GetLong(self):
        self.long = self.bytes_data[self.index:self.index+8]
        self.long = int.from_bytes(self.long, byteorder='little')
        self.index += 8
        print(f'指针位置{self.index}')
        return self.long
    
    # 获取字符串, 先取字符长度, 指针自动定位到字符串对应的bytes起始位置
    def GetString(self):
        self.String_length = self.GetInt()
        self.String = self.bytes_data[self.index:self.index + self.String_length]
        self.index += self.String_length
        print(f'指针位置{self.index}')
        self.String = self.String.decode(encoding='utf-8')
        return self.String
    
    # 获取 4 个字节的 float
    def Getfloat(self):
        self.floats = self.bytes_data[self.index:self.index+4]
        self.floats = struct.unpack('f', self.floats)[0]
        self.index += 4
        print(f'指针位置{self.index}')
        return round(self.floats, 4)
    
    # 获取 8 个字节的int
    def GetDouble(self):
        self.Double = self.bytes_data[self.index:self.index+8]
        self.Double = struct.unpack('f', self.Double)[0]
        self.index += 8
        print(f'指针位置{self.index}')
        return round(self.Double, 4)

