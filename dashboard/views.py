from django.shortcuts import render
from post.models import BlogPost
from django.core.paginator import Paginator

def dashboard(request):
    home = False
    posts_all = BlogPost.objects.all()
    paginator = Paginator(posts_all, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts':posts,'home':home}
    return render(request,'dashboard/dashboard.html',context)