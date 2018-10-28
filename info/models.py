import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Email(models.Model):
    address = models.EmailField()
    user = models.ForeignKey('PersonalInfo', related_name='emails', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.address, self.user.real_name)


class PhoneNumber(models.Model):
    MOBILE = 'Mobile'
    WORK = 'Work'
    HOME = 'Home'
    FAX = 'Fax'
    BEEPER = 'Beeper'
    OTHER = 'Other'

    TYPES = [
        (MOBILE, 'Mobile'),
        (WORK, 'Work'),
        (HOME, 'Home'),
        (FAX, 'Fax'),
        (BEEPER, 'Beeper'),
        (OTHER, 'Other')
    ]

    number = models.CharField(max_length=32)
    type = models.CharField(choices=TYPES, default=MOBILE, max_length=8)
    user = models.ForeignKey('PersonalInfo', related_name='phone_numbers', on_delete=models.CASCADE)

    def __str__(self):
        return '%s for %s' % (self.type, self.user.real_name)


class ExternalLink(models.Model):
    OTHER = 'external-link'
    SOUNDCLOUD = 'soundcloud'
    LINKEDIN = 'linkedin-square'

    CHOICES = [
        (OTHER, 'Other'),
        (SOUNDCLOUD, 'Soundcloud'),
        (LINKEDIN, 'LinkedIn'),
    ]

    url = models.URLField()
    url_type = models.CharField(max_length=16, choices=CHOICES, default=OTHER)
    title = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('PersonalInfo', related_name='external_links', on_delete=models.CASCADE)

    def __str__(self):
        if not self.title:
            return self.url
        return self.title


class NickName(models.Model):
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name='nick_names')
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s (%s)' % (self.user.real_name, self.name)


class PersonalInfo(models.Model):
    real_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.real_name


class Detail(models.Model):
    name = models.CharField(max_length=64)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class DetailItem(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='items')
    text = models.TextField()
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.detail.name


class Picture(models.Model):
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField()

    def __str__(self):
        return self.user.real_name


@receiver(post_delete, sender=Picture)
def remove_image_file(sender, instance, **kwargs):
    if os.path.exists(instance.image.file.name):
        os.remove(instance.image.file.name)
