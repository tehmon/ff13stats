import os
import time
from os import listdir
import pymem

pm = pymem.Pymem("ffxiii2img.exe")
b_address = pm.base_address

char_base = {
            "serah": pm.read_int(b_address+0x4D5B798), 
            "noel": pm.read_int(b_address+0x4D5B708)
            }
offsets = {"leader": 0xCA0 , "hp": 0xE18, "str": 0xE28 , "mag": 0xE2C}
files_in_dir = []

def create():
    if not os.path.exists("ff132_files"):
        os.mkdir("ff132_files")
    if not os.listdir("ff132_files"):
        for c in char_base:
            for s in offsets:
                file_name = "ff132_files/" + c + "_" + s + ".txt"
                with open(file_name, "w+") as f:
                    pass

def main():
    if not os.path.exists("ff132_files"):
        create()
    elif not listdir("ff132_files"):
        create()

    files_in_dir = [f for f in listdir("ff132_files")]
    while True:
        for file in files_in_dir:
            for c_key in char_base:
                if c_key in file:
                    file_path = f"ff132_files/{file}"
                    with open(file_path, "r+") as f:
                        for o_key in offsets:
                            if o_key in file:
                                if o_key == "leader":
                                    if "leader" in file:
                                        if pm.read_uchar(char_base[c_key]+offsets[o_key]) == 0:
                                            f.write("Leader")
                                            f.truncate()
                                        else:
                                            f.truncate(0)
                                else:
                                    f.write(str(pm.read_int(char_base[c_key]+offsets[o_key])))
                                    f.truncate()


if __name__ == "__main__":
    main()
