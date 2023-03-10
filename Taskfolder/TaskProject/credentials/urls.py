# from . import views
# from django.urls import path
#
# app_name='credentials'
#
# urlpatterns = [
#     path('register', views.register, name="register"),
#     path('login', views.login, name="login"),
#     path('logout',views.logout,name="logout"),
#     path('details',views.details,name="details"),
#     ]



from . import views
from django.urls import path
from .views import register,login,newpage,form,logout

urlpatterns = [

      path('register',views.register,name="register"),
      path('login',views.login,name="login"),
      path('newpage',views.newpage,name="newpage"),
      path('form',views.form,name='form'),
      path('logout',views.logout,name='logout'),
      path('message',views.message,name='message'),


]