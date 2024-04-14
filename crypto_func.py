# pip install pycryptodome

import os
import sys
import json
import hashlib

from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

from base64 import b64encode, b64decode

# generate key 
def generateKeyAES():
  return os.urandom(32)

def encrypt_file_aes(inputFile, outputFile, key):
  
  plaintexts  = inputFile.read()
    
  cipher = AES.new(key, AES.MODE_CTR) # dùng mode ctr: mode mạnh nhất
  
  ctBytes = cipher.encrypt(plaintexts)
  
  nonce = b64encode(cipher.nonce)
  
  ciphertexts = b64encode(ctBytes)
  
  result = json.dumps({'nonce':nonce.hex(), 'ciphertexts':ciphertexts.hex()})

  if outputFile == sys.stdout.buffer:
    print("The result encrypted file:")
  outputFile.write(result.encode())


def decrypt_file_aes(inputFile, outputFile, key):
  
  ctBytes = inputFile.read()

  try:

    b64 = json.loads(ctBytes)
    
    nonce = b64decode(bytes.fromhex(b64['nonce']))
    ciphertexts = b64decode(bytes.fromhex(b64['ciphertexts']))
    
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    message = cipher.decrypt(ciphertexts)

  except (ValueError, KeyError):
    print("Incorrect decryption")
  
  outputFile.write(message)

'''
key = generateKeyAES()
encrypt_file_aes('plaintext.txt', 'ciphertext.txt', key)
decrypt_file_aes('ciphertext.txt', 'message.txt', key)
'''

# Yeu cau A part 2

def generateRSAKey():
  key = RSA.generate(2048)
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
  return Kpublic.encrypt(plainTexts)

def decryptRSA(cipherTexts, Kprivate):
  return Kprivate.decrypt(cipherTexts)

'''
Kprivate, Kpublic = generateRSAKey()
plainTexts = 'hello, my name is long, trường khoa học tự nhiên'
cipherText = encryptRSA(plainTexts, Kpublic)
print('cipher: ', cipherText)
message = decryptRSA(cipherText, Kprivate)
print('message: ', message)
'''

def SHA256(Crypto_cipher_obj):
  return hashlib.sha256(Crypto_cipher_obj)

def SHA1(Crypto_cipher_obj):
  return Crypto_cipher_obj._hashObj.new().digest()

''' test
string = 'diug guyays dhwu shshu ahdh'
sha256 = SHA256(string.encode('utf-8'))
sha1 = SHA1(string.encode('utf-8'))

print('sha256: ', sha256.hexdigest())
print('sha1: ', sha1.hexdigest())
'''