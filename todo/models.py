from django.db import models

# Create your models here.
# If you need functionality from one class to be available in another
# all you need to do is inherit the one you need.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
