from django.urls import path
from .views import CreateAccountView, UserView

app_name = 'users'

urlpatterns = [
# Added a URL to the form to create new account page
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),   
# Added a UTL to the user profile page  
    path('<int:pk>/', UserView.as_view(), name='userProfile')
]