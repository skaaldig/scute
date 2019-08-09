import calendar
from django.db import models

class TimeStamp(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ActivityCategory(TimeStamp):
    class Meta:
        verbose_name_plural = "Activity Categories"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Principal(TimeStamp):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Activity(TimeStamp):
    class Meta:
        verbose_name_plural = "Activities"

    subject = models.CharField(max_length=255)
    account = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    contacts = models.TextField()
    category = models.ForeignKey(ActivityCategory, on_delete=models.SET_NULL, null=True)
    principal = models.ForeignKey(Principal, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.account} - {self.state}"


class ObjectCode(TimeStamp):
    code = models.CharField(max_length=4, unique=True) # Test unique
    short_desc = models.CharField(max_length=150)
    long_desc = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.short_desc}"


class Category(TimeStamp):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Expense(TimeStamp):
    # ADD EMPLOYEE 
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()

    activity = models.OneToOneField(Activity, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    code = models.ForeignKey(ObjectCode, on_delete=models.SET_NULL, null=True)
    receipt = models.ImageField()


    def __str__(self):
        return f"{self.code} - {self.date}"
