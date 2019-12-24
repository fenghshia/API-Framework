'''
加密算法与解密算法
'''
import base64
from Crypto.Cipher import AES


class AES_Generater():

    def __init__(self):
        # 密匙
        self.Key = 'UCyHhh7T4yWVWvoi'
        # 加密模式
        Model = AES.MODE_ECB
        # 生成加密对象
        self.AES_generater = AES.new(self.Key.encode('utf-8'), Model)
        # 去除填充算法
        self.UNPAD = lambda s: s[0:-ord(s[-1])]
        # 分片大小
        BS = 16
        # pkcs5填充算法
        self.PADDING = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)

    def AES_Encode(self, input_str):
        # 原始字符串进行填充转换字节流
        pad_byte = self.PADDING(input_str).encode('utf-8')
        # 加密
        AES_byte = self.AES_generater.encrypt(pad_byte)
        # base64编码后转换字符串
        return base64.encodebytes(AES_byte).decode('utf8').replace('\n', '')

    def AES_Decode(self, input_str):
        # 字符串转换字节流
        pad_byte = base64.decodebytes(input_str.encode('utf-8'))
        # 解密后转换字符串
        str_text = self.AES_generater.decrypt(pad_byte).decode('utf-8')
        return self.UNPAD(str_text)
