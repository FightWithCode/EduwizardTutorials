from django.db import models
from django.core.validators import RegexValidator

STATES = (
    ("Class VI", "Class VI",),
    ("Class VII", "Class VII",),
    ("Class VIII", "Class VIII",),
    ("Class IX", "Class IX",),
    ("Class X", "Class X",),
    ("Class XI", "Class XI",),
    ("Class XII", "Class XII",),
    ("Others", "Others",),
)


class JoinQuery(models.Model):
    name = models.CharField(max_length=25)
    mobile_regex = RegexValidator(regex=r'^\d{10}$', message="Please Enter Correct Mobile Number...")
    mobile_number = models.CharField(validators=[mobile_regex], max_length=10, blank=False)
    subject_or_class = models.CharField(max_length=50, choices=STATES)
    message = models.CharField(max_length=255)
	
    def __str__(self):
        return str(self.name + ' | ' + self.subject_or_class)


class NewsLetter(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email
