from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = [

    ('Cars', 'Cars'),
    ('Electronics', 'Electronics'),
    ('Phones', 'Phones'),
    ('Furniture', 'Furniture'),
]


class Listing(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    location = models.CharField(max_length=255)

    contact_details = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to='listing_images/',
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title