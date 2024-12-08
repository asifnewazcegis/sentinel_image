#image name format: t45rxj_09jan2021.img
# this code is compatible with python 2.7
# please input tile_name
tile_name = "45ryj"

import os
import re
import calendar

# use forward slash(/) in path directory
input_folder = "Z:/MOL007/Image/Sentinel_Image/2021"



avail_month = [] 
avail_year = []
# Iterate over all the directories and files
for folder_name, subfolders, filenames in os.walk(input_folder):
    #print(f'Folder: {folder_name}')
    for filename in filenames:
        if filename.endswith(".img") and filename.startswith(f"t{tile_name.lower()}"):     
            print(f'  File: {filename}')
            # Regular expression to match the month
            match = re.search(r'\d{2}([a-zA-Z]+)(\d{4})', filename)
            if match:
                month = match.group(1).capitalize()  # Extract and capitalize the month
                year = match.group(2)  # Extract the year
                avail_month.append(month)
                avail_year.append(year)
            else:
                pass

# Get the list of full month names (skip the first entry which is an empty string)
months = [month[:3] for month in calendar.month_name if month]
available_mnth = []
unavailable_mnth = []
for month in months:
    if month in avail_month:
       available_mnth.append(month)
    else:
        unavailable_mnth.append(month)
print("\navailable_mnth: {}".format(available_mnth),str(len(available_mnth))+"\n\n"+"unavailable_mnth: {}".format(unavailable_mnth),str(len(unavailable_mnth)))

avail_year = set(avail_year)
print("\n"+"year: {}".format(avail_year))

