# pip install pycryptodome

import os
import json
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

# generate key 
def generateKeyAES(keySize):
    key = os.urandom(int(keySize) // 8)
    return key

keySize = input('Enter ASE key size (bit): ')
key = generateKeyAES(keySize)
print('key: ', key.hex())

def encrypt_file_aes(input_file, output_file, key):
  """
  Mã hóa tập tin sử dụng thuật toán AES.

  Tham số:
    input_file (str): Đường dẫn đến tập tin đầu vào
    output_file (str): Đường dẫn đến tập tin đầu ra
    key (bytes): Khóa bí mật Ks

  Trả về:
    None
  """
  #cipher = AES.new(key, AES.MODE_)
  #nonce = cipher.nonce
  #ciphertext, tag = cipher.encrypt_and_digest(open(input_file, "rb").read())

  plaintexts  = open(input_file, "rb").read()
  cipher = AES.new(key, AES.MODE_CTR)
  ct_bytes = cipher.encrypt(plaintexts)
  nonce = b64encode(cipher.nonce).decode('utf-8')
  ct = b64encode(ct_bytes).decode('utf-8')
  result = json.dumps({'nonce':nonce, 'ciphertext':ct})


  with open(output_file, "wb") as f:
    f.write(result.encode())

def decrypt_file_aes(input_file, output_file, key):
  """
  Giải mã tập tin sử dụng thuật toán AES.

  Tham số:
    input_file (str): Đường dẫn đến tập tin đầu vào
    output_file (str): Đường dẫn đến tập tin đầu ra
    key (bytes): Khóa bí mật Ks

  Trả về:
    None
  """
  with open(input_file, "rb") as f:
    ct_bytes = f.read()

  try:
    b64 = json.loads(ct_bytes.decode())
    nonce = b64decode(b64['nonce'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    print('type: ', type(cipher))
    pt = cipher.decrypt(ct)
    print("The message was: ", pt)
  except (ValueError, KeyError):
    print("Incorrect decryption")
  with open(output_file, "wb") as f:
    f.write(pt)

encrypt_file_aes('D:\\Network Security\\plaintext.txt', 'D:\\Network Security\\ciphertext.txt', key)
decrypt_file_aes('D:\\Network Security\\ciphertext.txt', 'D:\\Network Security\\message.txt', key)