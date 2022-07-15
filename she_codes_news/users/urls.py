from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
# Added a URL to the form to create new account page
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),   
# Added a UTL to the user profile page  
    path('<int:pk>/', views.UserView.as_view(), name='userProfile')
]