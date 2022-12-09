#!/usr/bin/python3
# for the exiftool to work here, this program needs to be in the same folder of the extracted files

import os
import zipfile
import exiftool

# extract the files
print("EXTRACTING THE FILES")
location = "/home/kali/Downloads/tryhackme/"	# change this to the location of the .zip files
files_list = os.listdir(location)
for file in files_list:
        with zipfile.ZipFile(location + file, 'r') as zip:
                zip.extractall("/home/kali/Downloads/extracted")        # extracts the zip to this folder

# extract the metadata
print("EXTRACTING METADATA")
files = os.listdir(".") # lists the extracted files
with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(files)
metadata_file = open("metadata_file", "wt+")	# opens file to save the metadata
for d in metadata:
        metadata_file.write(f"{str(d)}\n")	# writes the metadata in a file (the metadata of this program is included)
print("FINISHED")
metadata_file.close()	# closes the file

