from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import MovieViewSets, RatingViewSets, UserViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSets)
router.register("ratings", RatingViewSets)
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
