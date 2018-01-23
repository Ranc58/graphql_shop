from django.db import models


class Product(models.Model):
        title = models.CharField(max_length=255)
        description = models.CharField(max_length=255, null=True, blank=True)
        is_published = models.BooleanField(default=False)
        category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)

        def __str__(self):
            return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
