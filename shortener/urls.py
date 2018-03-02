from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('<slug:slug>',views.short_url_redirect),
    path('shorten/',views.shorten_url)
]
