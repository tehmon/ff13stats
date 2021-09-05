import os
import time
from os import listdir
import pymem

pm = pymem.Pymem("ffxiiiimg.exe")
b_address = pm.base_address
try:
    inv_base = pm.read_int(b_address+0x28BF440)
    char_base = {
                "sazh": pm.read_int(b_address+0x28BF608), 
                "snow": pm.read_int(b_address+0x28BF638), 
                "fang": pm.read_int(b_address+0x28BF590), 
                "hope": pm.read_int(b_address+0x28BF5C0),
                "vanille": pm.read_int(b_address+0x28BF650), 
                "lightning": pm.read_int(b_address+0x28BF5F0)
                }
except:
    inv_base = pm.read_int(b_address+0x2402BE0)
    char_base = {
                "sazh": pm.read_int(b_address+0x2402DA8), 
                "snow": pm.read_int(b_address+0x2402DD8), 
                "fang": pm.read_int(b_address+0x2402D30), 
                "hope": pm.read_int(b_address+0x2402D60),
                "vanille": pm.read_int(b_address+0x2402DF0), 
                "lightning": pm.read_int(b_address+0x2402D90)
                }
inv_offsets = {"gil": 0x2578, "crystage": 0x258C}
offsets = {"hp": 0xDB8 , "str": 0xDC8 , "mag": 0xDCC}
files_in_dir = []

def create():
    if not os.path.exists("ff13_files"):
        os.mkdir("ff13_files")
    if not os.listdir("ff13_files"):
        for inv in inv_offsets:
            file_name = "ff13_files/" + inv + ".txt"
            with open(file_name, "w+") as f:
                pass
        for c in char_base:
            for s in offsets:
                file_name = "ff13_files/" + c + "_" + s + ".txt"
                with open(file_name, "w+") as f:
                    pass

def main():
    if not os.path.exists("ff13_files"):
        create()
    elif not listdir("ff13_files"):
        create()

    files_in_dir = [f for f in listdir("ff13_files")]
    while True:
        
        for file in files_in_dir:
            for inv in inv_offsets:
                if inv in file:
                    file_path = f"ff13_files/{file}"
                    with open(file_path, "r+")as f: 
                        f.write(str(pm.read_int(inv_base + inv_offsets[inv])))
                        f.truncate()
            for c_key in char_base:
                if c_key in file:
                    file_path = f"ff13_files/{file}"
                    with open(file_path, "r+") as f:
                        for o_key in offsets:
                            if o_key in file:
                                f.write(str(pm.read_int(char_base[c_key]+offsets[o_key])))
                                f.truncate()
if __name__ == "__main__":
    main()
