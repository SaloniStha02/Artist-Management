from django.db import models
from User.models import NewUser
from django.utils import timezone

class Song(models.Model):
    title=models.CharField(max_length=60)
    released_date=models.DateField(default=timezone.now,null=True)
    cover=models.ImageField(upload_to='', null=True, blank=True)
    is_deleted=models.BooleanField(default=False)
    artist=models.ForeignKey(NewUser,null=True,on_delete=models.CASCADE,related_name='songs')

    
    def __str__(self):
        return self.title
    
    def delete(self,hard_delete=False):
        if hard_delete:
            super().delete()
        else:
            self.is_deleted=True
            self.save()

    def restore(self):
        self.is_deleted=False
        self.save()

