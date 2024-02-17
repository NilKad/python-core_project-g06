import os
from pathlib import Path
import shutil
import sys

dir_suff_dict = {"Images": ['.jpeg', '.png', '.jpg', '.svg', '.bmp'],
                 "Video": [".avi", ".mp4", ".mov",  ".wkv",  ".mpg", ".mpeg"],
                 "Documents": [".doc", ".docx", ".txt", ".pdf",  ".xls", ".xlsx", ".pptx"],
                 "Audio": [".aac", ".mp3",  ".wav", ".wma"],
                 "Archives": [".zip", ".gz", ".tar", ".gztar", ".bztar", ".ztar"],
                 "Other": []
                 }


def normalize(word):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    Leter_kiril = []
    for leter in CYRILLIC_SYMBOLS:
        Leter_kiril.append(leter)
    for c, l in zip(Leter_kiril, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    word = word.translate(TRANS)
    i = 0
    for ch in word:
        if (ord(ch) >= ord('a') and ord(ch) <= ord('z')) or (ord(ch) >= ord('A') and ord(ch) <= ord('Z')) or (ord(ch) >= ord('0') and ord(ch) <= ord('9')) or ch == '_':
            i += 1
        else:
            word_l = list(word)
            word_l[i] = "_"
            word = ''.join(word_l)
            i += 1
    return word


known_suff = []
all_suff = []
v = 0


def sort_func(path_dir, v):
    cur_dir = Path(path_dir)
    dir_path = []

    for root, dirs, files in os.walk(path_dir):
        for d in dirs:
            dir_path.append(os.path.join(root, d))
        root_name = Path(root)
        if root_name.name in dir_suff_dict:
            continue
        for file in files:
            p_file = Path(root)/file
            name_normalize = f"{
                normalize(p_file.name[0:-len(p_file.suffix)])}{p_file.suffix}"
            p_file.rename(Path(root)/name_normalize)
            p_file = Path(root)/name_normalize
            for suff in dir_suff_dict:
                if p_file.suffix.lower() in dir_suff_dict[suff]:
                    if p_file.suffix.lower() not in known_suff:
                        known_suff.append(p_file.suffix.lower())
                    dir_img = cur_dir/suff
                    dir_img.mkdir(exist_ok=True)
                    if suff != "Archives":
                        try:
                            p_file.rename(dir_img.joinpath(p_file.name))
                        except FileExistsError:
                            p_file.rename(dir_img.joinpath(
                                f'{p_file.name.split(".")[0]}_c{p_file.suffix}'))
                            print(f"Possibly a duplicate: {p_file.name}")
                    else:
                        dir_archive = cur_dir/suff / \
                            p_file.name[0:-len(p_file.suffix)]
                        dir_archive.mkdir(exist_ok=True)
                        try:
                            shutil.unpack_archive(p_file, dir_archive)
                            os.remove(p_file)
                            sort_func(dir_archive, v=1)
                        except shutil.ReadError:
                            os.remove(p_file)
                            os.removedirs(dir_archive)
                else:
                    if p_file.suffix.lower() not in all_suff:
                        all_suff.append(p_file.suffix.lower())
    for root, dirs, files in os.walk(path_dir):
        if files != []:
            dir_img = Path(root)/"Other"
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
        for root, dirs, files in os.walk(path_dir):
            if files != []:
                print(f"{root}\\{files}")
        print(f"known extensions :{known_suff}")
        unknown_suff = list(set(all_suff) - set(known_suff))
        print(f"unknown extensions :{unknown_suff}")


def sort(path):
    try:
        path_d = path
        if not Path(path_d).exists():
            print("[-] Folder does not exist")
        else:
            sort_func(path_d, v=0)
            print("[!] Sorting complete")
    except IndexError:
        print("[-] Enter folder to sort !")

# if __name__ == "__main__":
#    path = 'E:\Example_Folder'
#    sort(path)
