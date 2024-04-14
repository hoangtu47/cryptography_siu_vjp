#!/usr/bin/python3

# for JSON file manipulation
import json

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

from base64 import b64encode, b64decode

# module for TextIO handle
import sys

# user-defined cryptophic tool module
import crypto_func

# module to handle command-line argument
import argparse

parser = argparse.ArgumentParser(
    description='Decrypt an encrypted file.',
    epilog='Made with love by Quoc Bao & Chau Long!'
)

parser.add_argument('infile',
    type=argparse.FileType("rb"),
    help='File path of encrypted file.'
)

parser.add_argument('metadata',
    type=argparse.FileType('rb'),
    help='File path of metadata storing Kx and SHA-1 of Kprivate.'
)

parser.add_argument( "-k", "--kprivatefile",
    nargs='?', 
    type=argparse.FileType("rb"),
    default= sys.stdin.buffer,
    help='File path of file storing the Kprivate key. If not specified, the standard input stream is used.'
)

parser.add_argument( "-o", "--outfile",
    nargs='?',
    type=argparse.FileType('wb'),
    default=sys.stdout.buffer,
    help='Desired file path for the decrypted file. If not specified, the standard output stream is used.'
)

args = parser.parse_args()

# --- subsection a. ---
RSA_Kprivate = RSA.import_key(args.kprivatefile.read())

privateKey = RSA_Kprivate.export_key('PEM')
Kprivate = RSA.importKey(privateKey)
Kprivate = PKCS1_OAEP.new(Kprivate)

# Kprivate SHA-1 checking
HKprivate = json.loads(args.metadata.read())

if crypto_func.SHA1(Kprivate).hex() != HKprivate["SHA-1"]:
    raise Exception("Kprivate key does not match!")

# In search for Ks key
Ks = crypto_func.decryptRSA(bytes.fromhex(HKprivate['Kx']), Kprivate)

crypto_func.decrypt_file_aes(args.infile, args.outfile, Ks)    

args.infile.close()
args.metadata.close()
args.outfile.close()
args.kprivatefile.close()