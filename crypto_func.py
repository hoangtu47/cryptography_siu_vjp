# pip install pycryptodome
import os
import json
import hashlib

from Cryptodome.Cipher import AES
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

from base64 import b64encode, b64decode

# generate key 
def generateKeyAES():
    keySize = input('Enter ASE key size (bit): ')
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
    message = cipher.decrypt(ciphertexts)
  except (ValueError, KeyError):
    print("Incorrect decryption")
  with open(outputFile, "wb") as f:
    f.write(message)

key = generateKeyAES()
encrypt_file_aes('plaintext.txt', 'ciphertext.txt', key)
decrypt_file_aes('ciphertext.txt', 'message.txt', key)

# Yeu cau A part 2

def generateRSAKey():
  keySize = input('Enter key size (bit): ')
  key = RSA.generate(int(keySize))
  # create public key
  publicKey = key.publickey().export_key('PEM')
  Kpublic = RSA.importKey(publicKey)
  Kpublic = PKCS1_OAEP.new(Kpublic)
  # create private key
  privateKey = key.export_key('PEM')
  Kprivate = RSA.importKey(privateKey)
  Kprivate = PKCS1_OAEP.new(Kprivate)
  return Kprivate, Kpublic

def encryptRSA(plainTexts, Kpublic):
  plainTexts = str.encode(plainTexts)
  return Kpublic.encrypt(plainTexts)

def decryptRSA(cipherTexts, Kprivate):
  return Kprivate.decrypt(cipherTexts)

Kprivate, Kpublic = generateRSAKey()
plainTexts = 'hello, my name is long, trường khoa học tự nhiên'
cipherText = encryptRSA(plainTexts, Kpublic)
print('cipher: ', cipherText)
message = decryptRSA(cipherText, Kprivate)
print('message: ', message)


def SHA256(string):
  return hashlib.sha256(string)
def SHA1(string):
  return hashlib.sha1(string)

# test
string = 'diug guyays dhwu shshu ahdh'
sha256 = SHA256(string.encode('utf-8'))
sha1 = SHA1(string.encode('utf-8'))

print('sha256: ', sha256.hexdigest())
print('sha1: ', sha1.hexdigest())