from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.PostList.as_view(), name='home'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about'),
	path('<slug:slug>/', views.detail, name='detail'),
]