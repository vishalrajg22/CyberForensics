import os
import hashlib
import binascii

def get_files(path):
    dir_list = os.listdir(path)
    return dir_list

def ntlm(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    hex = binascii.hexlify(content)
    input_str = str(hex)
    ntlm_hash = binascii.hexlify(hashlib.new('md4', input_str.encode('utf-16le')).digest()).decode("utf-8")
    return ntlm_hash

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha1(fname):
    hash_md5 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha256(fname):
    hash_md5 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha512(fname):
    hash_md5 = hashlib.sha512()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

main_dir = "./"
file_list = get_files(main_dir)
# print(file_list)
path_li = []
for file in file_list:
    if os.path.isdir(main_dir + file):
        path_li.append(main_dir + file + "/")

i = 0
for path in path_li:
    file_list = get_files(path)
    for file in file_list:
        i += 1
        file_path = path + file
        file_size = os.path.getsize(file_path)
        print("S. No:",i)
        print("File/State:", "empty")
        print("Name:", file)
        print("Filetype:",file.split(".")[1])
        print("File size:",file_size,"bytes")
        print("MD5:", md5(file_path))
        print("SHA1:", sha1(file_path))
        print("SHA256:", sha256(file_path))
        print("SHA512:", sha512(file_path))
        print("NTLM:",ntlm(file_path))
        print()