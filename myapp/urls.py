from .import views
from django.urls import path

urlpatterns = [
    path('',views.Home, name="first-page"),
    path('about/',views.about, name="about-page"),
    path('M/',  views.M,name="My"),
    path('register/', views.register, name="register")
]