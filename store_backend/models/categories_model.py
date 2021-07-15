from django.db import models

class Categories(models.Model):
    category = models.TextField(max_length= 50, unique=True)

    def __str__(self):
        return self.category
