"""User related data models"""
from typing import Optional, TYPE_CHECKING
from render.security import HashedPassword, get_password_hash
from pydantic import BaseModel, root_validator, Field
from fastapi import HTTPException, status
from pydantic.functional_validators import BeforeValidator

from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    """Represents the User Model"""

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    email: str = Field(...)
    username: str = Field(...)
    password: HashedPassword | str
    name: str = Field(...)


def generate_username(name: str) -> str:
    """Generates a slug username from a name"""
    return name.lower().replace(" ", "-")


class UserResponse(BaseModel):
    """Serializer for User Response"""

    name: str
    username: str
    dept: str
    avatar: Optional[str] = None
    bio: Optional[str] = None
    currency: str


class UserResponseWithBalance(UserResponse):
    balance: Optional[int] = None

    @root_validator(pre=True)
    def set_balance(cls, values: dict):
        """Sets the balance of the user"""
        instance = values["_sa_instance_state"].object
        values["balance"] = instance.balance
        return values


class UserRequest(BaseModel):
    """Serializer for User request payload"""

    name: str
    email: str
    dept: str
    password: str
    currency: str = "USD"
    username: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None

    @root_validator(pre=True)
    def generate_username_if_not_set(cls, values):
        """Generates username if not set"""
        if values.get("username") is None:
            values["username"] = generate_username(values["name"])
        return values


class UserProfilePatchRequest(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None


class UserPasswordPatchRequest(BaseModel):
    password: str
    password_confirm: str

    @root_validator(pre=True)
    def check_passwords_match(cls, values):
        """Checks if passwords match"""
        if values.get("password") != values.get("password_confirm"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )
        return values

    @property
    def hashed_password(self) -> str:
        """Returns hashed password"""
        return get_password_hash(self.password)
