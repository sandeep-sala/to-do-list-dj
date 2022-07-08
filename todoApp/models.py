from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Model definition for Task."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Task."""
        ordering = ["complete", ]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        """Unicode representation of Task."""
        return self.title

    # TODO: Define custom methods here
