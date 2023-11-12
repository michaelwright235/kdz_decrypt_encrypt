import os
import argparse
from Crypto.Cipher import ARC4
from Crypto.Hash import MD5

passwd_origin = ["" for x in range(13)]
passwd_origin[0] = "JS16bglqyz"
passwd_origin[1] = "CLU150ejnk"
passwd_origin[2] = "AEIPRW037c"
passwd_origin[3] = "47afilmpwx"
passwd_origin[4] = "BFH6cgkrvz"
passwd_origin[5] = "DGKMNOZ28k"
passwd_origin[6] = "CJQTX49eno"
passwd_origin[7] = "A03780ckwx"
passwd_origin[8] = "8ioqrtvwxy"
passwd_origin[9] = "LGCNSkang0"
passwd_origin[10] = "dy8913ksh7"
passwd_origin[11] = "KLNPQSVY03"
passwd_origin[12] = "b2PXfFSHv3"

def find_cipher(filesize):
    password = ""
    for i in range(len(filesize)):
        current_pswd = passwd_origin[len(filesize)-i-1]
        current_filesize_int = int(filesize[i])
        password += current_pswd[current_filesize_int & 0xf]
    key = MD5.new(bytes(password, 'ascii')).digest()
    RC4_Cipher = ARC4.new(key)
    return RC4_Cipher

def decrypt(filename_in, filename_out):
    if filename_out == None:
        filename_out = os.path.splitext(filename_in)[0]+'.cab'

    filesize = str(os.path.getsize(filename_in))
    RC4_Cipher = find_cipher(filesize)

    file_in = open(filename_in, 'rb')
    file_out = open(filename_out, "wb")

    header = file_in.read(4)
    header_decrypted = RC4_Cipher.decrypt(header)
    if header_decrypted != bytes("MSCF", 'ascii'): # cab file header
        print("Warning: decrypted CAB file may be incorrect")
    file_out.write(header_decrypted)

    chunk = file_in.read(1024)
    while chunk:
        original_data = RC4_Cipher.decrypt(chunk)
        file_out.write(original_data)
        chunk = file_in.read(1024)

    file_in.close()
    file_out.close()

def encrypt(filename_in, filename_out):
    if filename_out == None:
        filename_out = os.path.splitext(filename_in)[0]+'.kdz'

    filesize = str(os.path.getsize(filename_in))
    RC4_Cipher = find_cipher(filesize)

    file_in = open(filename_in, 'rb')
    file_out = open(filename_out, "wb")
    
    chunk = file_in.read(1024)
    while chunk:
        original_data = RC4_Cipher.encrypt(chunk)
        file_out.write(original_data)
        chunk = file_in.read(1024)

    file_in.close()
    file_out.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog = 'kdz.py',
                        description = 'Decrypt and encrypt KDZ files for old LG phones')
    parser.add_argument('-d', help='Decrypt KDZ file', action='store_true')
    parser.add_argument('-e', help='Encrypt CAB file', action='store_true')
    parser.add_argument('-o', help='Output filename. By default the converted file is saved in the same folder.', type=str)
    parser.add_argument('filename', help='Path to the file', type=str)
    args = parser.parse_args()

    if os.path.isfile(args.filename) == False:
        print("File doesn't exist")
        exit()

    if args.d == True:
        decrypt(args.filename, args.o)
        print("KDZ file has been successfully decrypted")
    elif args.e == True:
        encrypt(args.filename, args.o)
        print("CAB file has been successfully encrypted")
