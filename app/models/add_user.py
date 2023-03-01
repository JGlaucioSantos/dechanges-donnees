from hashlib import sha256
from getpass import getpass

from models import User
from models import CreateSession


SALT: str = "systemglaucio"

def encryption_password(password: str) -> str:
    return sha256(f"{SALT}{password.strip()}".encode()).hexdigest()

email: str = input("Enter an email for the new user:")
password: str = getpass("Enter a password for the new user:")

session = CreateSession.create_session()
user = User(email=email, password=encryption_password(password))
session.add(user)
session.commit()