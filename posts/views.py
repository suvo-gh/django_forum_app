from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):

    #save
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    #Show error if no
        else:
            return HttpResponseRedirect(form.errors.as_json())




    posts = Post.objects.all().order_by('-created_at')[:20]

    return render(request, 'posts.html', {'posts':posts})


def delete(request, post_id):
    #Find post and delete
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")