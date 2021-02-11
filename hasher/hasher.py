import os 
import hashlib, binascii
from dotenv import load_dotenv
load_dotenv()

def pablo_hasher(string, salt=None):
    
    if salt == None:
        # Generate a salt
        salt = os.urandom(32)
        
        # Hash the string
        hashed = hashlib.pbkdf2_hmac('sha256', string.encode('utf-8'), salt, 100000, dklen=128)

        return binascii.hexlify(hashed), binascii.hexlify(salt)
    
    else:
        # Hash the string
        hashed = hashlib.pbkdf2_hmac('sha256', string.encode('utf-8'), salt, 100000, dklen=128)

        return binascii.hexlify(hashed)