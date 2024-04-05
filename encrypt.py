#!/usr/bin/python3

# module for file manipulation
import os

# user-defined cryptophic tool module
import crypto_func

# module to handle command-line argument
import argparse

parser = argparse.ArgumentParser(
    description='Encrypt a file using AES and RSA algorithm.',
    epilog='Made with love by Quoc Bao & Chau Long!'
)

parser.add_argument('filepath',
    help='File path of plaintext file.'
)

parser.add_argument( "-k", "--kprivatefile",
    help='File path of new file storing the Kprivate key. If the provided file path is not valid, newly created one',
)

parser.add_argument( "-o", "--output",
    help='Desired file path for the encrypted file.'
)

args = parser.parse_args()

# --- subsection a. ---
# check the plaitext file path for validity
if not os.path.exists(args.filepath):
    raise FileNotFoundError(f"The file '{args.filepath}' does not exist.")

# --- subsection b. ---
# Ks private key generation 
# TODO

# Encrypt the provided file using AES
# TODO

# Store the encrypted file

# Check if the output file was specified if not then ask for input
if args.output is not None:
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    fd = open(args.output, 'w')
else:
    output = input("Enter output file path: ")
    # create the directory if not already existed
    os.makedirs(os.path.dirname(output), exist_ok=True)

    fd = open(output, 'w')

# write encrypted file to output file
# TODO

fd.close()

# --- subsection c. ---

# Generation of Kprivate and Kpublic using RSA
# TODO

# encrypt Ks using Kpublic
# TODO 

# print out Kx
# TODO

# --- subsection d. ---
# write Kx to file, along with it SHA-1
with open('./metadata/C.metadata', 'w') as file:
    # TODO
    pass

# --- subsection e. ---

# Exprt Kprivate key
if args.kprivatefile is not None:
    os.makedirs(os.path.dirname(args.kprivatefile), exist_ok=True)
    with open(args.kprivatefile, 'w') as file:
        # Write Kprivate to file
        # TODO
        pass
else:
    # Print Kprivate in std.out
    # TODO
    pass