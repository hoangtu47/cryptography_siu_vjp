# Module to store function definations 
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import hashlib

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