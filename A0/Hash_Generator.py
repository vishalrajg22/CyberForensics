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
data_li = []
data_types = []
data_state = []
for path in path_li:
    file_list = get_files(path)
    for file in file_list:
        dict = {}
        # i += 1
        file_path = path + file
        file_size = os.path.getsize(file_path)
        # print("S. No:",i)
        dict["File/State"] = path[2:-1]
        dict["Name"] = file
        dict["Filetype"] = file.split(".")[1]
        dict["File size"] = str(file_size) + " bytes"
        dict["MD5"] = md5(file_path)
        dict["SHA1"] = sha1(file_path)
        dict["SHA256"] = sha256(file_path)
        dict["SHA512"] = sha512(file_path)
        dict["NTLM"] = ntlm(file_path)
        data_li.append(dict)
        data_types.append(file.split(".")[1])
        data_state.append(path[2:-1])

data_types = sorted(list(set(data_types)))
data_state = sorted(list(set(data_state)))

i = 0
for dt in data_types:
    for state in data_state:  
        for data in data_li:
            if data["Filetype"] == dt and data["File/State"] == state :
                i += 1
                print("S. No:",i)
                print("File/State:", data["File/State"])
                print("Name:", data["Name"])
                print("Filetype:", data["Filetype"])
                print("File size:", data["File size"])
                print("MD5:", data["MD5"])
                print("SHA1:", data["SHA1"])
                print("SHA256:", data["SHA256"])
                print("SHA512:", data["SHA512"])
                print("NTLM:", data["NTLM"])
                print()