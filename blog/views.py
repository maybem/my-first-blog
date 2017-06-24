"""from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from .models import Post
def post_list(request):
	return render(request,'blog/post_list.html',{})


#def another(request):
#	return HttpResponse("Ala ma kota, ale na innym widoku")"""
"""
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})"""

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})