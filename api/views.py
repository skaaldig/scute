from django.shortcuts import render
from rest_framework import viewsets

from expenses import models
from . import serializers


class PrincipalViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for viewing or editing Principals
    """ 
    queryset = models.Principal.objects.all()
    serializer_class = serializers.PrincipalSerializer


class ObjectCodeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for viewing or editing Expense Object Codes
    """ 
    queryset = models.ObjectCode.objects.all()
    serializer_class = serializers.ObjectCodeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for viewing or editing Expense Categories
    """ 
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ActivityCategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for viewing or editing Activity Categories
    """ 
    queryset = models.ActivityCategory.objects.all()
    serializer_class = serializers.ActivityCategorySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for viewing or editing Expense Categories
    """ 
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for viewing or editing Expenses
    """ 
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
