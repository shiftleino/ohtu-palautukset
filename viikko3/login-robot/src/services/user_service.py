from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise InvalidCredentialsError("Username already exists")

        if not re.match("^[a-z]{3,}$", username):
            raise InvalidCredentialsError("Invalid username")

        if not re.match(".*[^a-zA-Z].*", password) or len(password) < 8:
            raise InvalidCredentialsError("Invalid password")
