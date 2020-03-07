from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import User, Post

# Create your views here.
def users(request):
    return render(request, 'users/users.html', {
        'users': User.objects.all()
    })

def profile(request, user_id):
    return render(request, 'users/profile.html', {
        'user': get_object_or_404(User, pk = user_id),
        'posts': get_list_or_404(Post, user = User.objects.get(pk = user_id))
    })


