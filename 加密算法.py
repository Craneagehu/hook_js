import base64

# base64加密算法，解密算法
# 想将字符串转编码成base64,要先将字符串转换成二进制数据
# url = "https://www.cnblogs.com/songzhixue/"
# bytes_url = url.encode("utf-8")
# str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
# print(str_url)
#
# # 将base64解码成字符串
# url = "aHR0cHM6Ly93d3cuY25ibG9ncy5jb20vc29uZ3poaXh1ZS8="
# str_url = base64.b64decode(url).decode("utf-8")
# print(str_url)


# -------------------------------------------------------------------
# AES对称加密及解密算法
from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
# 加密
key = 'a cdefjhgaaaaaaa'.encode('utf-8')
# 生成向量
iv = Random.new().read(AES.block_size)
print(iv)
obj = AES.new(key=key,mode=AES.MODE_CFB,iv=iv)
# 这里密钥key 长度必须为16（AES-128）,
# 24（AES-192）,或者32 （AES-256）Bytes 长度
# 目前AES-128 足够目前使用
message = '斌彬'.encode()
ciphertext = obj.encrypt(message)
# 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
# 所以这里统一把加密后的字符串转化为16进制字符串
ciphertext=b2a_hex(ciphertext)
print(ciphertext)

# 解密
obj2 = AES.new(key,AES.MODE_CFB,iv=iv)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
detext = obj2.decrypt(a2b_hex(ciphertext))
print(detext.decode())


# --------------------------------------------------
'''
    一般的rsa加密通常会先声明一个rsa对象
    本地使用公钥加密即public key
    通常有Encrypt关键字
    加密后字符长度为128位或256位
    结合以上套路可以帮助我们快速判断加密方式如何,便于我们理清解密思路。
'''
# RSA加密及解密
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

message = 'async'   # 消息原文

# 初始化RSA对象
rsa = RSA.generate(1024,Random.new().read) # 伪随机数生成器
# 生成私钥
private_key = rsa.exportKey()
# 生成公钥
public_key = rsa.publickey().exportKey()
# 打印私钥和公钥
print(private_key.decode())
print(public_key.decode())

# 将私钥和公钥存入对应名称的文件
with open('private.pem','wb') as f:
    f.write(private_key)

with open('public.pem','wb') as f:
    f.write(public_key)

with open('public.pem','r') as f:
    # 从文件中加载公钥
    pub = f.read()
    pubkey = RSA.importKey(pub)
    # 用公钥加密消息原文
    cipher = PKCS1_v1_5.new(pubkey)
    c = base64.b64encode(cipher.encrypt(message.encode())).decode()

with open('private.pem','r') as f:
    # 从文件中加载私钥
    pri = f.read()
    prikey = RSA.importKey(pri)
    # 用私钥解密消息密文
    cipher = PKCS1_v1_5.new(prikey)
    m = cipher.decrypt(base64.b64decode(c),'error').decode()
print('消息原文：%s\n消息密文：%s\n解密结果：%s' % (message,c,m))