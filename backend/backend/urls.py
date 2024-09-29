from django.urls import path
from app import views  # replace 'app' with the name of your app folder
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),  # Enables the admin interface
    path('', views.submit_url, name='home'),
    path('templates/submit-url/', views.submit_url, name='submit_url'),
    path('urls/', views.url_list, name='url_list'),
    path('api/submit-url/', views.submit_url_api, name='submit_url_api'),  # New process endpoint
]
