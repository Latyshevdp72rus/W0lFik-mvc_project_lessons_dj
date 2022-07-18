from django.urls import path
from .views import create_user,login_user,user_logout

urlpatterns = [
    path('registration/', create_user),
    path('login/', login_user),
    path('logout/', user_logout),

]
