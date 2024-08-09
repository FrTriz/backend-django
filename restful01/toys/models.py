from django.db import models

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=150, blank=False, default="")
    description = models.CharField(max_length=250, blank=False, default="")
    release_date = models.DateTimeField()
    toy_category = models.CharField(max_length=208, default="")
    was_included_in_home = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)
    
    def _str_(self):
        return self.name