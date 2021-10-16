import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.crypto import get_random_string


def upload_obfuscated_filename(instance, orig_filename):
    _filename, _ext = os.path.splitext(orig_filename)
    _fn = get_random_string(length=8)
    return f"{_fn}{_ext}"


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Email(models.Model):
    class Meta:
        ordering = ["-primary", "address"]

    primary = models.BooleanField(default=False)
    address = models.EmailField(max_length=255)
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.address


class PhoneNumber(models.Model):
    primary = models.BooleanField(default=False)
    number = models.CharField(max_length=32)
    fa_class = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name='phone_numbers')

    def __str__(self):
        return f"{self.user}"


class Picture(models.Model):
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name="pictures")
    picture = models.ImageField(max_length=255, upload_to=upload_obfuscated_filename)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class DetailCategory(models.Model):
    class Meta:
        verbose_name_plural = "Detail Categories"
        ordering = ["sort_order"]

    user = models.ForeignKey("PersonalInfo", on_delete=models.CASCADE, related_name="detail_categories")
    name = models.CharField(max_length=255)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class DetailItem(models.Model):
    class Meta:
        ordering = ["sort_order"]

    detail_category = models.ForeignKey(DetailCategory, on_delete=models.CASCADE, related_name="detail_items")
    text = models.CharField(max_length=255)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.detail_category.name


class PersonalInfo(SingletonModel):
    class Meta:
        verbose_name_plural = "Personal Info"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employer(models.Model):
    user = models.ForeignKey("PersonalInfo", on_delete=models.CASCADE, related_name="employers")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employment(models.Model):
    YEAR = '%Y'
    MONTH = '%Y-%m'
    DAY = '%M-%m-%d'

    CHOICES = [
        (YEAR, 'Year'),
        (MONTH, 'Month'),
        (DAY, 'Day')
    ]

    NORMAL = ''
    INTERNSHIP = 'Internship'
    FREELANCER = 'Freelancer'
    SELF_EMPLOYED = 'Self employed'
    SUMMER_JOB = 'Summer job'

    STATUS_CHOICES = [
        (NORMAL, 'Normal'),
        (INTERNSHIP, 'Internship'),
        (FREELANCER, 'Freelancer'),
        (SELF_EMPLOYED, 'Self Employed'),
        (SUMMER_JOB, 'Summer job')
    ]

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='employments')
    title = models.CharField(max_length=255, blank=True, null=True)
    date_start = models.DateField()
    date_start_display_resolution = models.CharField(max_length=8, choices=CHOICES, default=DAY)
    date_end = models.DateField(blank=True, null=True)
    date_end_display_resolution = models.CharField(max_length=8, choices=CHOICES, default=DAY)
    employment_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=NORMAL, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employer.name} ({self.date_start} - {self.date_end if self.date_end else ''})"


class EmploymentTask(models.Model):
    class Meta:
        ordering = ["sort_order"]

    employment = models.ForeignKey(Employment, related_name='employment_tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.employment.employer.name} ({self.employment.date_start} - {self.employment.date_end if self.employment.date_end else ''})"


class Hobby(models.Model):
    class Meta:
        verbose_name_plural = "Hobbies"

    user = models.ForeignKey("PersonalInfo", on_delete=models.CASCADE, related_name="hobbies")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class HobbyItem(models.Model):
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name='hobby_items')
    text = models.TextField()
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.hobby.name


class ExternalLink(models.Model):
    class Meta:
        ordering = ["sort_index"]
    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name='external_links')
    url = models.URLField()
    fa_class = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    sort_index = models.IntegerField(default=0)

    def __str__(self):
        if not self.title:
            return self.url
        return self.title


@receiver(post_delete, sender=Picture)
def remove_image_file(sender, instance, **kwargs):
    try:
        os.remove(instance.picture.file.name)
    except FileNotFoundError:
        pass
