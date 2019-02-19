from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'new_user', views.new_user, name='new_user'),
    url(r'logout', views.logout_user, name='logout'),
]
