from django.db import models
from datetime import datetime, date
class ShowManager(models.Manager):
    def basic_validations(self, postData):
        errors = {}
        title = Show.objects.filter(title=postData['title'])
        if len(postData['title']) < 2:
            errors['title'] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters"
        if len(postData['desc']) < 3 and len(postData['desc']) > 0:
            errors['desc'] = "Show description should be at least 10 characters"
        if datetime.strptime(postData['rel_date'], '%Y-%m-%d') > datetime.today():
            errors['date'] = "Release date must be a valid date"
        if len(title)>0:
            errors['title_check'] = "This show is already on the database"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
