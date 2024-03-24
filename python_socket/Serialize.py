'''
PutBytes    --int (1个字节)
PutBool     --bool (1个字节)
PutShort    --Short (2个字节)
PutInt      --int (4个字节)
PutLong     --long (8个字节)
PutString   --str (先取字符串长度, 然后调用Putint, 再将str.encode()写进去)
Putfloat    --float (struct.pack,   4个字节)
PutDouble   --Double (8个字节)
'''

import struct

class Assemble(object):

    # 初始化bytes对象, 接收数据
    def __init__(self) -> bytes:
        self.bytes_data = bytes()

    # int类型  --1个字节
    def PutBytes(self, ints):
        self.bytes_data += ints.to_bytes(1, byteorder='little')[::-1]
    
    # Bool类型 --1个字节
    def PutBool(self, bool):
        if bool:
            self.bool_bytes = 1
            self.bytes_data += self.bool_bytes.to_bytes(1, byteorder='little')[::-1]
        else:
            self.bool_bytes = 0
            self.bytes_data += self.bool_bytes.to_bytes(1, byteorder='little')[::-1]

    # int类型 --2个字节
    def PutShort(self, shortnum):
        self.shortint_bytes = shortnum.to_bytes(2, byteorder='little')[::-1]
        self.bytes_data += self.shortint_bytes

    # int类型 --4个字节
    def PutInt(self, num):
        self.num_bytes = num.to_bytes(4, byteorder='little')[::-1]
        self.bytes_data += self.num_bytes
    
    # int类型 --8个字节
    def PutLong(self, longnum):
        self.longnum_bytes = longnum.to_bytes(8, byteorder='little')[::-1]
        self.bytes_data += self.longnum_bytes

    # str类型 
    def PutString(self, string):
        self.PutInt(len(string))
        self.string_bytes = string.encode(encoding='utf-8')
        self.bytes_data += self.string_bytes

    # float类型, 4个字节
    def Putfloat(self, float):
        self.float_bytes = struct.pack('<f', float)[::-1]
        self.bytes_data += self.float_bytes

    # int类型 8个字节
    def PutDouble(self, doublenum):
        self.doublenum_bytes = struct.pack('<f', doublenum)[::-1]
        self.bytes_data += self.doublenum_bytes

    # CG_verify数据
    def CG_verifyResult(self):

        # 加密
        self.encryption = 0
        self.encryption_bytes = self.encryption.to_bytes(1, byteorder='little')[::-1]

        # 消息长度
        self.bytes_data_length =len(self.bytes_data)
        self.bytes_data_length_bytes = self.bytes_data_length.to_bytes(4, byteorder='little')[::-1]
        
        # CG_verify数据 = 加密 + 消息长度 + 消息体
        self.bytes_data = self.encryption_bytes + self.bytes_data_length_bytes + self.bytes_data
        return self.bytes_data
    
    def Result(self):
        return self.bytes_data
    

