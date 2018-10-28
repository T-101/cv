from django.db import models


class Hobby(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class HobbyItem(models.Model):
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name='hobbyitems')
    text = models.TextField()
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.hobby.name
