from django.contrib import admin

from expenses import models

@admin.register(models.Activity, models.ActivityCategory, models.Principal)
class ActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Expense, models.Category, models.ObjectCode)
class ExpenseAdmin(admin.ModelAdmin):
    pass