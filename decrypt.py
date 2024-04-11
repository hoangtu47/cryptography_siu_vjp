#!/usr/bin/python3

# module for file manipulation
import os

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
    type=argparse.FileType('r'),
    help='File path of encrypted file.'
)


# a workaround to enable the program to print the prompt string before asking for input
# this function print the prompt string prior to return sys.stdin
def foo():
    print('Please enter Kprivate key:', end=' ', flush=True)
    return sys.stdin

parser.add_argument( "-k", "--kprivatefile",
    nargs='?', 
    type=argparse.FileType('r'),
    default=foo(),
    help='File path of file storing the Kprivate key.'
)

parser.add_argument( "-o", "--outfile",
    nargs='?',
    type=argparse.FileType('w'),
    default=sys.stdout,
    help='Desired file path for the decrypted file.'
)

args = parser.parse_args()

# --- subsection a. ---

with args.infile as file:
    # read file content
    encrpyted_data = file.read()

# --- subsection b. ---

# extract Kprivate key
# either from file or user input
with args.kprivatefile as file:
    KPrivate = file.readline().strip()
    print('Successfully fetch kprivate input')
    print(KPrivate)

# --- subsection c. ---

# Key processing
# TODO

# --- subsection d. ---

# Key processing
# TODO

# --- subsection e. ---
with args.outfile as file:
    file.write("successfully print output file\n")
