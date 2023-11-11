import hashlib
import argparse
from os import walk
from json import dump

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-o", "--output",help="text file output directory", default=".")
parser.add_argument("-n", "--name", help="output file name", default="md5")
parser.add_argument("-f", "--folder",action="store_true",help="is folder", default=False)
parser.add_argument("-j", "--json", action="store_true", help="output to json", default=False)
parser.add_argument("src", help="Source location")
args = parser.parse_args()
config = vars(args)
output_file = f'{config.get("output")}\\{config.get("name")}'
isJson, isFolder = config.get("json"),config.get("folder")
file = config.get("src")
def fileList(folder):
    directories= []
    out = []
    files1 = []
    for root, dirs, files in walk(folder):
        directories.append(root)
        
        files1.append(files)
        for file in files:
            out.append(root + "\\" + file)
    return out 
folder = fileList(file)    
def md5(fname):
    hash_md5 = hashlib.md5()
    hashes = []
    if not isFolder:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hashes.append(hash_md5.hexdigest())
    else:
        for file in folder:
            with open(file, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            hashes.append(hash_md5.hexdigest())
    return hashes
def writeToText(hashes):
    if isJson:
        dict_out = {}
        for hash in hashes:
            if isFolder:
                index = hashes.index(hash)
                dict_out[f"{folder[index]}"] = hash
            else:
                dict_out = {file: hash}
        with open(f"{output_file}.json", "w", encoding="utf-8") as f:
                dump(dict_out, f, ensure_ascii=False, indent=4)
    else:
        with open(f"{output_file}.txt", "w", encoding="utf-8") as f:
            for hash in hashes:
                if isFolder:
                    index = hashes.index(hash)
                    f.write(f"{folder[index]} : {hash}\n")
                else:
                    f.write(f"{file} : {hash}\n")
writeToText(md5(file))
