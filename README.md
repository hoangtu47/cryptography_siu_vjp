# CSC11115 - cryptography_siu_vjp

```diff
! Due: Sunday, 14 April, 09:00 PM
```

# About

These two scripts, `encrypt.py` and `decrypt.py`, as their name suggest, perform precisely AES algorithm encryption and decryption upon file and RSA algorithm operations upon keys.    

## Authors
***21120414** - Hà Quốc Bảo*

***21120096** - Hồ Châu Long*

## Report collaboration [link](https://docs.google.com/document/d/1z0BT401Mage-i2W1t0aYn4j23skpkmeDKtINnO6-sJI/edit?usp=sharing)

## Project detailed description
![Detailed description of CSC11115's cryptographic project](https://github.com/21120414/cryptography_siu_vjp/assets/117193418/68c08bb2-257a-4cad-a8d6-8cc800b812c1)

## Set up and run

### Requirements

- Python == 3.11.2
- pycryptodome == 3.20.0

### Run the application

This application is CLI-driven designed. Two functionalities, namely encrypting and decrypting, are splited into two seperate scripts. `encrypt.py` and `decrypt.py`.

For the scripts to run properly, an Python interpreter must be specified, either by setting the shebang to the desired interpreter (such as that of a Python virtual environment), or implicitly use `python3` command prior to the scripts, as the system will automatically pick the current environment interpreter.

The second way to run is better. Because when the scripts are moved across different environments, the shebang which specifying the interpreter's path is no longer valid as the interpreter's path of different environments aren't the same. Thus, in the example bellow, we shall use the second approach to run the application.


### Help

As many other common command, those commands are equipped with `-h, --help` option to provide useful information of usage. 

## Usage and example

### Encrypt a file

```
usage: python3 encrypt.py [-h] [-k [KPRIVATEFILE]] [-o [OUTPUT]] infile

Encrypt a file using AES algorithm , key using RSA algorithm.

positional arguments:
  infile                File path of plaintext file.

options:
  -h, --help            show this help message and exit
  -k [KPRIVATEFILE], --kprivatefile [KPRIVATEFILE]
                        File path of new file to store the Kprivate
                        key. If not specified, the standard output
                        stream is used.
  -o [OUTPUT], --output [OUTPUT]
                        Desired file path for the decrypted file.
                        If not specified, the standard output
                        stream is used.
 ```


### Decrypt a file

```
usage: decrypt.py [-h] [-k [KPRIVATEFILE]] [-o [OUTFILE]]
                  infile metadata

Decrypt an encrypted file.

positional arguments:
  infile                File path of encrypted file.
  metadata              File path of metadata storing Kx and SHA-1
                        of Kprivate.

options:
  -h, --help            show this help message and exit
  -k [KPRIVATEFILE], --kprivatefile [KPRIVATEFILE]
                        File path of file storing the Kprivate key.
                        If not specified, the standard input stream
                        is used.
  -o [OUTFILE], --outfile [OUTFILE]
                        Desired file path for the decrypted file.
                        If not specified, the standard output
                        stream is used.
```

### Example
