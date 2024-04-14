#!/usr/bin/python3

# module for file manipulation
import os

# to manipulate JSON file
import json

# module for TextIO handle
import sys

# user-defined cryptophic tool module
import crypto_func

# module to handle command-line argument
import argparse

parser = argparse.ArgumentParser(
    description='Encrypt a file using AES and RSA algorithm.',
    epilog='Made with love by Quoc Bao & Chau Long!'
)

parser.add_argument('infile',
    type=argparse.FileType('rb'),
    help='File path of plaintext file.'
)

parser.add_argument( "-k", "--kprivatefile",
    nargs='?',
    type=argparse.FileType('wb'),
    # To write or read binary data from/to the standard streams
    default=sys.stdout.buffer,                
    help='File path of new file to store the Kprivate key.',
)

parser.add_argument( "-o", "--output",
    nargs='?',
    type=argparse.FileType('wb'),
    # To write or read binary data from/to the standard streams
    default=sys.stdout.buffer,
    help='Desired file path for the decrypted file.'
)

args = parser.parse_args()

# --- subsection a + b. ---

# Ks private key generation 
KsKey = crypto_func.generateKeyAES()

# Encrypt the provided file using AES
# Store the encrypted file
crypto_func.encrypt_file_aes(args.infile, args.output, KsKey)

# --- subsection c. ---

# Generation of Kprivate and Kpublic using RSA
Kprivate, Kpublic = crypto_func.generateRSAKey()

# encrypt Ks using Kpublic
Kxkey = crypto_func.encryptRSA(KsKey, Kpublic)

# --- subsection d. ---
# write Kx to file, along with it SHA-1 as hex format to prevent conversion like UTF-8
HKprivate = json.dumps({'Kx':Kxkey.hex(), 'SHA-1':crypto_func.SHA1(Kprivate).hex()})

with open("metadata/{}.metadata".format(os.path.basename(sys.argv[1])), 'wb') as file:
    file.write(HKprivate.encode())

if args.kprivatefile == sys.stdout.buffer:
    print("KPrivate key:")
args.kprivatefile.write(Kprivate._key.export_key())


args.infile.close()
args.kprivatefile.close()
args.output.close()