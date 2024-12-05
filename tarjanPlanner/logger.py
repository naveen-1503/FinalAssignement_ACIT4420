#logger.py
from datetime import datetime
#decorator that logs the changes done
def log_function_call(func):
    def wrapper(*args, **kwargs):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Prepare the log entry for function call
        log_message = (
            f"==========\n"
            f"Timestamp: {timestamp}\n"
            f"Function: {func.__name__}\n"
            f"Arguments: args={args}, kwargs={kwargs}\n"
            f"==========\n"
        )

        with open ("logger.txt", "a") as log_file:
            log_file.write(log_message)

        #Creates the result value
        result = func(*args, **kwargs)
        result_message = (
            f"Return Value: {result}\n"
            f"----------\n"
        )
        with open("logger.txt", "a") as log_file:
            log_file.write(result_message)
        return result
    return wrapper

