import os
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models import Prefetch
from django.db.models.functions import Lower
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django_extensions.db.fields import AutoSlugField

from PIL import Image


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
        primary_images_prefetch = Prefetch(
            "images",
            queryset=PortfolioImage.objects.filter(type=PortfolioImage.ImageChoices.PRIMARY),
            to_attr="primary_images"
        )
        item_prefetch = Prefetch(
            "portfolio_items",
            queryset=PortfolioItem.objects
            .filter(visible=True)
            .prefetch_related(primary_images_prefetch)
            .order_by(Lower("title")))

        prefetch_items = [
            "employers",
            "employers__employments",
            "employers__employments__employment_tasks",
            "detail_categories",
            "detail_categories__detail_items",
            "hobbies",
            "hobbies__hobby_items",
            "external_links",
            item_prefetch,
            "portfolio_items__tags",
        ]
        obj, created = cls.objects.prefetch_related(*prefetch_items).get_or_create(pk=1)
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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

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


class PortfolioItem(models.Model):
    class UrlTypes(models.TextChoices):
        NONE = ''
        LIVE = 'Live'
        DEMO = 'Demo'

    user = models.ForeignKey('PersonalInfo', on_delete=models.CASCADE, related_name='portfolio_items')
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    techniques = models.ManyToManyField('PortfolioTechniques', related_name='items', blank=True)
    url = models.URLField(blank=True, null=True)
    url_type = models.CharField(max_length=16, choices=UrlTypes, default=UrlTypes.NONE, blank=True, null=True)
    repository = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField('PortfolioItemTag', related_name='items', blank=True)
    visible = models.BooleanField(default=True)

    def get_primary_image(self):
        if hasattr(self, "primary_images") and self.primary_images:
            return self.primary_images[0]
        return None

    def __str__(self):
        return self.title


class PortfolioItemTag(models.Model):
    tag = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='tag')

    def __str__(self):
        return self.tag


class PortfolioTechniques(models.Model):
    technique = models.CharField(max_length=255)

    def __str__(self):
        return self.technique


class PortfolioImage(models.Model):
    class ImageChoices(models.TextChoices):
        PRIMARY = 'Primary'
        DESKTOP = 'Desktop'
        MOBILE = 'Mobile'

    item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='images')
    type = models.CharField(max_length=16, choices=ImageChoices, default=ImageChoices.PRIMARY)
    image = models.ImageField(upload_to=upload_obfuscated_filename)
    thumbnail = models.ImageField(upload_to=upload_obfuscated_filename, blank=True, null=True)

    def _create_thumbnail(self):
        if not hasattr(self.image.file, "content_type"):
            # If no new file was selected, the existing is used with some attributes missing.
            # This will also prevent the file being compressed over and over again.
            # The Screenshot pre_save signal also has a workaround,
            # so it will not delete existing files when no new file is selected
            return
        image = Image.open(self.image.file.file)
        image.thumbnail(size=(400, 400))
        image_file = BytesIO()
        image.save(image_file, image.format)
        thumbnail = BytesIO()
        image.save(thumbnail, image.format, quality=90)
        self.thumbnail.save(
            self.image.name,
            InMemoryUploadedFile(
                file=thumbnail,
                name=None,
                field_name='',
                content_type=self.image.file.content_type,
                size=image.size,
                charset=self.image.file.charset
            ),
            save=False
        )

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self._create_thumbnail()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item.title


@receiver(post_delete, sender=Picture)
def remove_image_file(sender, instance, **kwargs):
    try:
        os.remove(instance.picture.file.name)
    except FileNotFoundError:
        pass


@receiver(pre_delete, sender=PortfolioImage)
def delete_screenshot_file(sender, instance, **kwargs):
    # Use os.remove() as to not trigger pre_save signal for Screenshot
    try:
        if instance.image:
            os.remove(instance.image.path)

    except FileNotFoundError:
        pass
    try:
        if instance.thumbnail:
            os.remove(instance.thumbnail.path)

    except FileNotFoundError:
        pass
