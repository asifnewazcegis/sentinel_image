import os
import re
import calendar
import shutil

# Source and destination paths
source_path = r"D:\sentinel image\all_img"
# destination path will be longer to 2021 or 2022 or 2023
destination_path = r"Z:\MOL007\Image\Sentinel_Image\2021"

# Create a dictionary for month mappings
month_mapping = {f"{i:02}": calendar.month_name[i][:3] for i in range(1, 13)}

all_files = []

# Collect all files from the source directory
for root, dirs, files in os.walk(source_path):
    for file in files:
        all_files.append(file)
#print("Files collected:", all_files)

# Process each file
for file in all_files:
    if file.endswith(('.img', '.tif', '.rrd', '.aux', '.ovr')):
        match = re.search(r'(\d{2})([a-zA-Z]+)(\d{4})', file)
        if match:
            month = match.group(2).capitalize()
            year = match.group(3)  # Extract the year
            file_path_source = os.path.join(source_path, file)
            #print(file_path_source)           
            # Construct the new directory path based on month and year
            for num, mnth in month_mapping.items():
                num_mnth = f"{num}_{mnth}"
                #print(num_mnth)                
                if month in num_mnth:
                    new_path = os.path.join(destination_path, num_mnth)
                    new_file_path = os.path.join(new_path, file)  # Destination file path
                    #print("N-1: ",new_path)
                    #print("N_2: ",new_file_path)
                    # Create the destination directory if it doesn't exist
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                    if not os.path.exists(new_file_path) and os.path.exists(file_path_source):
                        try:
                            #shutil.copy(file_path_source, new_file_path)
                            shutil.move(file_path_source, new_file_path)
                            print(f"{file}: File copied successfully to {new_path}")
                        except Exception as e:
                            print(f"Error copying {file}: {e}")
                    else:
                        print(f"{file}: Source and destination represent the same file or file already exists.")
