from django.db import models


class Tool(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    memory = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    redPrice = models.CharField(max_length=50, null=True, blank=True)

    img_url = models.URLField(null=True, blank=True)

    productCode = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    screen_diagonal = models.TextField(null=True, blank=True)
    screen_resolution = models.TextField(null=True, blank=True)
    specifications = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'