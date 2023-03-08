import os
from distutils.dir_util import copy_tree, remove_tree

# DATA_FOLDER = "C:/Users/user/Documents/python_project/TempData"
# OUTPUT_FOLDER = "C:/Users/user/Documents/python_project/TempDataCopy"
DATA_FOLDER = "D:/CshsTempData"
OUTPUT_FOLDER = "D:/CshsTempDataCopy"

if not os.path.exists(DATA_FOLDER):
    os.mkdir(DATA_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

while True:
    print("請輸入指令")
    print("[copy] 複製數據")
    print("[exit] 離開程式")
    cmd = input().lower()
    
    if not cmd:
        print("必須輸入指令")
    elif cmd == 'exit':
        break
    elif cmd == 'copy':
        try:
            remove_tree(OUTPUT_FOLDER)
            copy_tree(DATA_FOLDER, OUTPUT_FOLDER)
        except Exception as ex:
            print(str(ex))
            break
    else:
        print(f'{cmd} 不是有效的指令')
