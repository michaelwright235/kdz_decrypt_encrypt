# KDZ Decrypt/Encrypt

This python script helps with decrypting and encrypting **old** KDZ files. They were used as a container of firmware for **old** LG phones, such as KP500, GS290, KS360, etc (models from around 2008-2010).

```text
usage: kdz.py [-h] [-d] [-e] [-o O] filename

Decrypt and encrypt KDZ files for old LG phones

positional arguments:
  filename    Path to the file

options:
  -h, --help  show this help message and exit
  -d          Decrypt KDZ file
  -e          Encrypt CAB file
  -o O        Output filename. By default the converted file is saved in the same folder.
```

Before running the script install dependencies via `pip install -r requirements.txt` command.

## What is a KDZ file?

A KDZ file is an [RC4](https://en.wikipedia.org/wiki/RC4) encrypted CAB archive file. The key is based on the file size and a special string, that was found in the original DLL file for decrypting those files. After determining the key, it's hashed with MD5 algorithm. Newer KDZ files use some other type of encryption.
