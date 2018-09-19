from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employment(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    internship = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    def __str__(self):
        if self.date_end:
            return '%s (%s - %s)' % (self.employer.name, self.date_start, self.date_end)
        return '%s (%s - )' % (self.employer.name, self.date_start)


class EmploymentTask(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sort_index = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)

    def __str__(self):
        if self.employment.date_end:
            return '%s (%s - %s)' % (
            self.employment.employer.name, self.employment.date_start, self.employment.date_end)
        return '%s (%s - )' % (self.employment.employer.name, self.employment.date_start)
