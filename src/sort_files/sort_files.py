import os
from pathlib import Path

dir_suff_dict = {"Images": ['.jpeg', '.png', '.jpg', '.svg', '.bmp'],
                 "Video": [".avi", ".mp4", ".mov",  ".wkv",  ".mpg", ".mpeg"],
                 "Documents": [".doc", ".docx", ".txt", ".pdf",  ".xls", ".xlsx", ".pptx"],
                 "Audio": ['.aac', '.adt', '.adts','.mp3',".wav", ".wma"],
                 "Archives": [".zip", ".gz", ".tar", ".gztar", ".bztar", ".ztar", '.rar'],
                 "Python": [".py"],
                 "EXE": ['.exe', '.bat', '.msi'],
                 "Other": []
                 }
known_suff = []
all_suff = []
v = 0


def sort_func(path_dir, dst_path, v):
    cur_dir = Path(path_dir)
    next_dir = Path(dst_path)
    dir_path = []

    for root, dirs, files in os.walk(path_dir):
        for d in dirs:
            dir_path.append(os.path.join(root, d))
        root_name = Path(root)
        if root_name.name in dir_suff_dict:
            continue
        for file in files:
            p_file = Path(root)/file
            for suff in dir_suff_dict:
                if p_file.suffix.lower() in dir_suff_dict[suff]:
                    if p_file.suffix.lower() not in known_suff:
                        known_suff.append(p_file.suffix.lower())
                    dir_img = next_dir/suff
                    dir_img.mkdir(exist_ok=True)
                    try:
                        p_file.rename(dir_img.joinpath(p_file.name))
                    except FileExistsError:
                        p_file.rename(dir_img.joinpath(
                            f'{p_file.name.split(".")[0]}_c{p_file.suffix}'))
                        print(f"Possibly a duplicate: {p_file.name}")
                else:
                    if p_file.suffix.lower() not in all_suff:
                        all_suff.append(p_file.suffix.lower())
    for root, dirs, files in os.walk(path_dir):
        if files != []:
            dir_img = Path(dst_path)/"Other"
            dir_img.mkdir(exist_ok=True)
            for file in files:
                p_file = Path(root)/file
                p_file.rename(dir_img.joinpath(p_file.name))
        break
    for dir_p in reversed(dir_path):
        if os.path.split(dir_p)[1] in dir_suff_dict or os.stat(dir_p).st_size != 0:
            continue
        else:
            try:
                os.rmdir(dir_p)
            except OSError:
                continue
    if v == 0:
        for root, dirs, files in os.walk(dst_path):
            if files != []:
                print(f"{root}\\{files}")
        print(f"known extensions :{known_suff}")
        unknown_suff = list(set(all_suff) - set(known_suff))
        print(f"unknown extensions :{unknown_suff}")


def sort(src_path, dst_path):
    if not Path(dst_path). exists():
        print(f'[!!!] Created Folder {dst_path}')
        Path(dst_path).mkdir(exist_ok=True)
    try:
        if not Path(src_path).exists():
            print("[-] Folder does not exist")
        else:
            sort_func(src_path, dst_path, v=0)
            print(f"[!] Sorting complete in folder {dst_path}")
    except IndexError:
        print("[-] Enter folder to sort !")