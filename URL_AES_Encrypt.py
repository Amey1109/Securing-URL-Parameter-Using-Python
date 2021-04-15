from AES import encrypt_AES_GCM
import binascii,os

secretKey = os.urandom(32)
msg = b'100'

encryptedID = encrypt_AES_GCM(msg,secretKey)
URL = "https://localhost/forgetPassword/" + (binascii.hexlify(encryptedID[0])).decode("utf-8")

print(URL)

