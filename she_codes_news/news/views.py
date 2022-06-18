from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story_order = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = story_order[:4]
        context['all_stories'] = story_order
        return context

# Added a view for a single story
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# Added a view to use the form configured in forms.py
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    #Added to automatically take the logged in user's username as author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)