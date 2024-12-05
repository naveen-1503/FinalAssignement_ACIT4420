#permissions.py
import os

def ensure_directory_access(directory):
    #  Ensure the directory exists and has proper permissions.
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    # Check write permission
    if not os.access(directory, os.W_OK):
        try:
            # Attempt to change permissions to allow writing
            os.chmod(directory, 0o755)  # rwxr-xr-x
        except PermissionError as e:
            raise PermissionError(f"Cannot modify directory permissions: {e}")