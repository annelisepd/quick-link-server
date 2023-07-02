from django.db import models
from django.http import HttpRequest

# Create your models here.

class Redirect(models.Model):
    key = models.CharField(max_length=10)
    url = models.TextField()

    def __str__(self):
        return self.key

    def access_count(self):
        return Access.objects.filter(redirect=self).count()
    
    def register_access(self, request: HttpRequest):
        remote_addr = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        Access.objects.create(
            ip=remote_addr,
            user_agent=request.META.get('HTTP_USER_AGENT'),
            redirect=self
        )

class Access(models.Model):
    creation = models.DateTimeField(auto_now=True)
    ip = models.CharField(max_length=39)
    user_agent = models.CharField(max_length=100)
    redirect = models.ForeignKey(Redirect, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip
