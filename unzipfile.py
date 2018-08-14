#!/usr/bin/python3

import shutil,os, gzip

destination_dir = '/media/ajaykpat/Ajay_W/Lakshya/PYTHON/KPI/temp/'
extension = ".gz"

os.chdir(destination_dir) # change directory from working dir to dir with files

for item in os.listdir(destination_dir): # loop through items in dir
    if item.endswith(extension): # check for ".gz" extension
        source_file = os.path.abspath(item) # get full path of files
        base=os.path.basename(item)  # this is for destination file name.
        os.path.splitext(base)       # remove the .gz extention
        destination_file = os.path.splitext(base)[0]
        with gzip.open(source_file,"rb") as f_in, open(destination_file,"wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

for item in os.listdir(destination_dir):
    if item.endswith(".gz"):
        os.remove(item)
