# Case 1: Create a Folder

import os
 
# def create_folder_demo(foldername):
#     os.mkdir(foldername)
 
# create_folder_demo("D:/DEMO/PLAYWRIGHT")

# Case 2: Create Nested Folders
# import os
 
# def create_nested_folders(nestedfolderpath):
#     os.makedirs(nestedfolderpath)
 
# create_nested_folders("D:/DEMO/A/B/C/D/E/F/G")

# Case 3: Rename an existing Folder to new Name
# import os
 
# def rename_existing_folder(oldfoldername, newfoldername):
#     os.rename(oldfoldername, newfoldername)
 
# rename_existing_folder("D:/DEMO/PLAYWRIGHT","D:/DEMO/PLAYPYTHONTESTIONG")

# Case 4: Remove an Existing Folder or Directory
# import os
 
# def remove_existing_folder(foldername):
#     os.rmdir(foldername)
 
# remove_existing_folder("D:/DEMO/PLAYPYTHONTESTIONG")

# Case 5: Remove Multiple Existing Folders or Directories
# import os
 
# def remove_multiple_folders(folderpath):
#     os.removedirs(folderpath)
 
# remove_multiple_folders("D:/DEMO/A/B/C/D/E/F/G")
 
# Case 5: File Collections, It should display only the Files.
 
# import os
# def file_collections_demo(folderpath):
#     dirs=os.listdir(folderpath)
 
#     for filename in dirs:
#         full_path=folderpath + filename
 
#         if(os.path.isfile(full_path)==True):
#             print(full_path)
 
 
 
# file_collections_demo("D:/DEMO/")

# Case 6: In a List of 'N' Numbers Files Delete only .csv Files
# import os
 
# def delete_all_csv_files(folderpath):
#     dirs=os.listdir(folderpath)
 
#     for filename in dirs:
#         full_path= folderpath + filename
#         if(os.path.isfile(full_path)==True):
#             if(full_path.endswith(".csv")):
#                 print(full_path)
#                 os.remove(full_path)
 
 
# delete_all_csv_files("D:/DEMO/")

# Case 7: Folder Collections
import os
 
def folder_collections_demo(folderpath):
    dirs=os.listdir(folderpath)
 
    for foldername in dirs:
        full_path=folderpath + foldername
        if(os.path.isdir(full_path)==True):
            print(full_path)

folder_collections_demo("D:/DEMO/")