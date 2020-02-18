from django.db import models
import datetime

class TVshowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "TV show title should be at least 2 characters."
        if TVshow.objects.get(title = postData['title']):
            errors['title_unique'] = "TV title already exist."
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters."
        if postData['release_date'] > str(datetime.date.today()):
            errors['release_date'] = "Release date should be in the past."
        if postData['desc']:
            if len(postData['desc']) < 10:
                errors['desc'] = "Description should be at least 10 characters."
        return errors


class TVshow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    desc = models.TextField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVshowManager()