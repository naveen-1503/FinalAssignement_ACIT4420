#logger.py
import datetime

#Logging the sent message
def log_file_movement(file, folder):
    try:
        with open ('message_log.txt', "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} {file} moved to folder {folder}\n")
    except IOError as e:
        print(f"Failed to write to log file: {e}")

if __name__ == "__main__":
    file = "test.py"
    folder = ".py" 
    log_file_movement(file, folder)