from django.db import models
class Image(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/img/%y")

    def __str__(self):
        return self.caption 