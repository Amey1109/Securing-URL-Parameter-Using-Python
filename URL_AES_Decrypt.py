from URL_AES_Encrypt import secretKey,encryptedID
from AES import decrypt_AES_GCM

decryptedID = decrypt_AES_GCM(encryptedID, secretKey)

print("This is ID : ",decryptedID.decode("utf-8"))