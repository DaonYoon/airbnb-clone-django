from django.db import models


# Create your models here.
class House(models.Model):
    """Model Definition for House."""

    name = models.CharField(max_length=140)
    # 무조건 양수일경우 포스티브 씀
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed? (애완동물)",
        default=True,
        help_text="Is pet allowed in the house?",
    )

    def __str__(self):
        return self.name
