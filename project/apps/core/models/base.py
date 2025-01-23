from django.db import models
import uuid
from core.constants import BaseVerboseNames


class BaseModel(models.Model):
    """
    Abstract base model for all application models.
    """

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        verbose_name=BaseVerboseNames.ID,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=BaseVerboseNames.CREATED_AT
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=BaseVerboseNames.UPDATED_AT
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self) -> str:
        """
        String representation of the model instance.
        """
        return f"{self.__class__.__name__} - {self.id}"
