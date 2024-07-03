from string import ( punctuation, whitespace, digits, ascii_lowercase, ascii_uppercase )
from datetime import datetime, timedelta

from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
