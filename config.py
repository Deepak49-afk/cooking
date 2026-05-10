import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-for-cooing-dev'
    # Use mongodb://localhost:27017/cooing as default connection
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/cooing'
    # Upload folder for local file storage
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    # Max file size: 16 MB
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
