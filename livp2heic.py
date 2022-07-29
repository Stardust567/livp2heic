#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile
import shutil

def unzip_file(file_name):
    zip_file = zipfile.ZipFile(file_name)
    if not os.path.isdir(file_name + "_files"):
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names, file_name + "_files/")
    zip_file.close()

def handle_livp(livp_path, mov_path, heic_path):
    if not os.path.isdir(mov_path):
        os.mkdir(mov_path)
    if not os.path.isdir(heic_path):
        os.mkdir(heic_path)
    livp_count, mov_count, heic_count = 0, 0, 0
    
    for file_name in os.listdir(livp_path):
        if file_name.endswith(".livp"):
            unzip_file(file_name)
            livp_count += 1
            mov_error, heic_error = True, True
            for tempfile in os.listdir("./" + file_name + "_files/"):
                if tempfile.endswith(".mov"):
                    oldfile = "./" + file_name + "_files/" + tempfile
                    newfile = mov_path + file_name.rstrip(".livp") + ".mov"
                    shutil.copyfile(oldfile, newfile)
                    mov_count += 1
                    mov_error = False
                elif tempfile.endswith(".heic"):
                    oldfile = "./" + file_name + "_files/" + tempfile
                    newfile = heic_path + file_name.rstrip(".livp") + "." + tempfile.split(".")[-1]
                    shutil.copyfile(oldfile, newfile)
                    heic_count += 1
                    heic_error = False
            if mov_error or heic_error:
                print("ERROR: " + file_name + " unzip faild.")

            shutil.rmtree("./" + file_name + "_files/")
    print("Unzip {} livpFile, get {} movFile & {} heicFile.".format(livp_count, mov_count, heic_count))


if __name__ == '__main__':
    # args: current_livp_path, unzip_mov_path, unzip_heic_path
    handle_livp(".", "./mov/", "./heic/")