from django.urls import path

from . import views

urlpatterns = [
    path('', views.model_form_upload, name='model_form_upload'),
    path('query/',views.search_query, name='search_query')
]