import logging
import os
from datetime import datetime

# Define log directory
logs_dir = os.path.join(os.getcwd(), "logs")

# Debugging: Print directory path
print(f"Log directory path: {logs_dir}")

# Ensure the directory is created
try:
    os.makedirs(logs_dir, exist_ok=True)
    print(f"Directory '{logs_dir}' created or already exists.")
except Exception as e:
    print(f"Error creating directory: {e}")

# Define log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Debugging: Print log file path
print(f"Log file path: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

