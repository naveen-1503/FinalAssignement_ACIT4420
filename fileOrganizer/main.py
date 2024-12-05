#main.py

from sortFiles import sortFiles
import os
import logging
from logger import log_file_movement

def main():
    inpDirectory = input("What Directory do you want to sort? ")
    
    #Checks if director exist
    if not os.path.exists(inpDirectory):
        logging.error(f"Directory {inpDirectory} does not exist.")
        return

    try:
        #Sorts the files
        sorted_files = sortFiles(inpDirectory)

        for sorted_file in sorted_files:
            #logs the sorting
            logging.info(f"Organized files: ")
            log_file_movement(sorted_file["file"], sorted_file["newDirectory"])
            
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()