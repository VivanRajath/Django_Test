from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    video_picture = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title

