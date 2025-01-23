from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from core.models import BaseModel
from user.constants import UserErrorMessages, UserVerboseNames


class UserManager(BaseUserManager):
    def create_user(self, email: str, username: str, password: str = None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError(UserErrorMessages.EMAIL_REQUIRED)

        if not username:
            raise ValueError(UserErrorMessages.USERNAME_REQUIRED)

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email: str, username: str, password: str = None
    ) -> "User":
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Custom user model with email as the unique identifier
    """

    email = models.EmailField(
        verbose_name=UserVerboseNames.EMAIL,
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=UserVerboseNames.USERNAME,
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=UserVerboseNames.IS_ACTIVE,
    )
    is_staff = models.BooleanField(
        default=False, verbose_name=UserVerboseNames.IS_STAFF
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        """
        String representation of the user
        """
        return self.email

    @property
    def is_superuser(self) -> bool:
        """
        Returns True if the user is a superuser
        """
        return self.is_staff

    class Meta:
        verbose_name = UserVerboseNames.VERBOSE_NAME
        verbose_name_plural = UserVerboseNames.VERBOSE_NAME_PLURAL
