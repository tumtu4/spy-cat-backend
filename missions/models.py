from django.db import models
from cats.models import Cat


class Mission(models.Model):
    cat = models.OneToOneField(
        Cat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mission"
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission #{self.id}"


class Target(models.Model):
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name="targets"
    )
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.country})"
