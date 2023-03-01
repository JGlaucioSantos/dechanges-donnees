
from settings.configs import Configs

from hashlib import sha256
from random import sample as sp
from secrets import token_hex

from fastapi import Response
from fastapi.requests import Request

from models.models import User
from models.models import CreateSession


configs = Configs()

class Encryption:

    def encryption_password(password: str) -> str:
        return sha256(f"{configs.SALT}{password.strip()}".encode()).hexdigest()


class AllowsAccess:

    def allows_access(email: str, password_hash: str) -> bool:
        try:
            session = CreateSession.create_session()
            data_database = session.query(User).filter(User.email == email).one_or_none()
            if data_database:
                email_database = str(data_database.email)
                password_database = str(data_database.password)
                email_user = email
                password_user = password_hash
            else:
                return False

            if email_database.strip() == email_user.strip() and password_database.strip() == password_user.strip():
                return True
            else:
                return False
        except Exception as _:
            return False


class Auth:

    def apply_auth(request: Request, response: Response) -> bool:
        try:
            cookie: str = request.cookies.get("_auth_cookie", None)
            if not cookie:
                cookie = f"{token_hex(16)}{''.join(sp(token_hex(32),16))}"
                response.set_cookie(
                    "_auth_cookie",
                    value=f"{cookie}"
                )
                return True
            return False
        except Exception as _:
            return False


    def remove_auth(request: Request, response: Response) -> bool:
        try:
            cookie: str = request.cookies.get("_auth_cookie", None)
            if cookie:
                response.delete_cookie("_auth_cookie")
                return True
            return False
        except Exception as _:
            return False


    def exists_auth(request: Request) -> bool:
        try:
            cookie: str = request.cookies.get("_auth_cookie", None)
            if cookie:
                return True
            return False
        except Exception as _:
            return False