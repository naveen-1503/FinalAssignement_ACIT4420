#sortFiles.py
import os
import re
from permissions import ensure_directory_access

#Dictonary with the file categories and the extensions related to each directory
file_categories = {
    "images": [r".*\.(jpg|jpeg|png|gif|bmp|tiff)$"],
    "documents": [r".*\.(docx|doc|pdf|txt|csv|xlsx|pptx)$"],
    "videos": [r".*\.(mp4|mkv|mov|avi|wmv)$"],
    "music": [r".*\.(mp3|wav|aac|flac)$"],
    "archives": [r".*\.(zip|rar|7z|tar|gz|bz2)$"],
}

#Decorator that adds a default category
def add_default_category(default="others"):
    def decorator(func):
        def wrapper(file_name):
            category1 = func(file_name)
            return category1 or default
        return wrapper
    return decorator

@add_default_category()
#Categorizes the files and returns the category
def categorized_files(file_name):
    for category, extenstions in file_categories.items():
        for pattern in extenstions:
            #Checks if the file match the the regex in FILE_CATEGORIES
            if re.match(pattern, file_name, re.IGNORECASE):
                return category
    return None

def sortFiles(directory):
    file_info = []

    #Makes sure the file has the correct permissions
    ensure_directory_access(directory)

    #Iterate through the files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory,file_name)

        #Checks if it is not at file, the code should just continue
        if not os.path.isfile(file_path):
            continue

        category = categorized_files(file_name)
        file_dir = os.path.join(directory, category)
        
        
        #Creates an directory if it doesn't exist
        os.makedirs(file_dir, exist_ok=True)
        
        file_full = os.path.join(file_dir, file_name)

        #Moves the file to the new subfolder
        os.replace(file_path, file_full)

        file_info.append({
            "file": file_name,
            "newDirectory": file_full 
        })
    
    return file_info
    

if __name__ == "__main__":
    sortFiles("../FileOrganizerRun")