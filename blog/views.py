from django.shortcuts import render ,get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
    #blogs = Blog.objects.all() # for getting the all blogs
    blogs = Blog.objects.order_by('-date') #for sortinf the blogs - getting the latest blogs
    #blogs = Blog.objects.order_by('-date')[:1]  #for liminting the blogs and getting last five records
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
