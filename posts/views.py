from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new


# Function based view for the home page
"""def home(request):

    posts = Post.objects.all()
    context = {'posts':posts}

    return render(request, 'home.html', context)"""