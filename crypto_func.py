# pip install pycryptodome
import os
import json
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

# generate key 
def generateKeyAES(keySize):
    key = os.urandom(int(keySize) // 8)
    return key

def encrypt_file_aes(inputFile, outputFile, key):
  # đọc file nhị phân
  plaintexts  = open(inputFile, "rb").read()
  cipher = AES.new(key, AES.MODE_CTR) # dùng mode ctr: mode mạnh nhất
  ctBytes = cipher.encrypt(plaintexts)
  nonce = b64encode(cipher.nonce).decode('utf-8')
  ciphertexts = b64encode(ctBytes).decode('utf-8')
  result = json.dumps({'nonce':nonce, 'ciphertexts':ciphertexts})


  with open(outputFile, "wb") as f:
    f.write(result.encode())

def decrypt_file_aes(inputFile, outputFile, key):
  with open(inputFile, "rb") as f:
    ctBytes = f.read()

  try:
    b64 = json.loads(ctBytes.decode())
    nonce = b64decode(b64['nonce'])
    ciphertexts = b64decode(b64['ciphertexts'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    print('type: ', type(cipher))
    message = cipher.decrypt(ciphertexts)
    print("The message was: ", message)
  except (ValueError, KeyError):
    print("Incorrect decryption")
  with open(outputFile, "wb") as f:
    f.write(message)

keySize = input('Enter ASE key size (bit): ')
key = generateKeyAES(keySize)
print('key: ', key.hex())
encrypt_file_aes('plaintext.txt', 'ciphertext.txt', key)
decrypt_file_aes('ciphertext.txt', 'message.txt', key)