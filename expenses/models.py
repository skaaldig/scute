from django.db import models


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ObjectCode(TimeStamp):
    code = models.CharField(max_length=4)
    short_desc = models.CharField(max_length=150)
    long_desc = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.short_desc}"


class Category(TimeStamp):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Expense(TimeStamp):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    code = models.ForeignKey('ObjectCode', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.date}"
