from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ("patient", "patient"),
    ("new_patient", "new_patient"),
    ("partially_recovered", "partially_recovered"),
    ("fully_recovered", "fully_recovered"),
)


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField(auto_now=False)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Appointments'


class Reviews(models.Model):
    name = models.CharField(max_length=50)
    review_tag = models.CharField(max_length=50)
    review = models.CharField(max_length=200)
    image = models.ImageField(upload_to='review')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Reviews'
