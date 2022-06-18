from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
# Configure a URL for a single story view
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
# Configure a URL for the form to create story
    path('add-story/', views.AddStoryView.as_view(), name='newStory')
]
