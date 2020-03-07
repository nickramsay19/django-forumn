from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponse

from users.models import User, Post

# Create your views here.
def posts(request):
    return render(request, 'posts/posts.html', {
        'posts': Post.objects.all()
    })

def post(request, post_id):
    return render(request, 'posts/post.html', {
        'post': get_object_or_404(Post, pk = post_id)
    })