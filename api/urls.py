from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"expense", views.ExpenseViewSet)
router.register(r"activity", views.ActivityViewSet)
router.register(r"activity-category", views.ActivityCategoryViewSet)
router.register(r"category", views.CategoryViewSet)
router.register(r"object-code", views.ObjectCodeViewSet)
router.register(r"principal", views.PrincipalViewSet)


urlpatterns = [
    path("", include(router.urls)),
]