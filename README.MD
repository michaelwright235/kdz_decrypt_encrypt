# KDZ Decrypt/Encrypt
This python script decrypts and encrypts KDZ files, which were used as a container of firmware for **old** LG phones, such as KP500, GS290, KS360, etc (models from around 2008-2010).

```
usage: kdz.py [-h] [-d] [-e] [-o O] filename

Decrypts or encrypts KDZ files for old LG phones

positional arguments:
  filename    Path to a file

options:
  -h, --help  show this help message and exit
  -d          Decrypt KDZ file
  -e          Encrypt CAB file
  -o O        Output filename. By default converted file is saved in the same folder.
```

Before running the script install dependecies via `pip install -r requirements.txt` command.

## What is a KDZ file?
A KDZ file is an encrypted CAB archive file. Encryption method is RC4. A key is based on file size and a special string, which was found in original .DLL for decrypting those files.
