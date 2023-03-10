from django.urls import path
from . import views
app_name='taskapp'

urlpatterns = [
    path('', views.home, name='home'),
    # path('submit',views.submit,name='submit'),
]