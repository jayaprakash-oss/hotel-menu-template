from django.urls import path
from .import views

urlpatterns = [
   path('register',views.register,name='register'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),
   
]


# temp_cart-->modules
# id,pcode.username,timestamp


#add to cart
# item add to cart 
