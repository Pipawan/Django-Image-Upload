from django.db import models


class Image(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption


class ImageUploadCounter(models.Model):
    ip_address = models.CharField(max_length=255)
    upload_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"IP Address: {self.ip_address}, Upload Count: {self.upload_count}"
