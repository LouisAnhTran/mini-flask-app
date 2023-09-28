import os

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_USERNAME=os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD=os.getenv('MONGO_DB_PASSWORD')
PORT=os.getenv('PORT')
MONGO_DB_DATABASE=os.getenv('MONGO_DB_DATABASE')