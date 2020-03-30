from django.views.generic import ListView
from .models import Post

class IndexPageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = "posts"

    #this is example, how to work ListView
    """
    def get_queryset(self):
        Post.objects.all()
        return super().get_queryset()
    """
    # example sql query
    #SELECT text FROM Post;
    # context_object_name = "object_list"
    # {"object_list": Post.objects.all()}