from django.db import models

# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
