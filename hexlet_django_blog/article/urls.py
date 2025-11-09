from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="articles_list"), 
    path("<int:id>/", views.IndexView.as_view(), name="article_detail"),
]