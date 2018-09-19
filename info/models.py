from django.db import models


class PersonalEmail(models.Model):
    address = models.EmailField()
    user = models.ForeignKey('PersonalInfo', related_name='emails', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.address, self.user.real_name)


class PersonalPhoneNumber(models.Model):
    HOME = 'Home'
    WORK = 'Work'
    MOBILE = 'Mobile'
    FAX = 'Fax'
    BEEPER = 'Beeper'
    OTHER = 'Other'

    TYPES = [
        (0, HOME),
        (1, WORK),
        (2, MOBILE),
        (3, FAX),
        (4, BEEPER),
        (5, OTHER)
    ]

    number = models.CharField(max_length=32)
    type = models.SmallIntegerField(choices=TYPES)
    user = models.ForeignKey('PersonalInfo', related_name='phonenumbers', on_delete=models.CASCADE)

    def __str__(self):
        return '%s for %s' % (self.TYPES[self.type][1], self.user.real_name)


class ExternalLink(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

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

    def __str__(self):
        return self.real_name
