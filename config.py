import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database path
DB_PATH = os.path.join(BASE_DIR, 'ims.db')

# Image directory
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

# Bill directory
BILL_DIR = os.path.join(BASE_DIR, 'bill')
