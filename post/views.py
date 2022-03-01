from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from .models import BlogPost
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from post.models import Comment
from forms import CommentForm,PostForm,ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.conf import settings

def postAll(request):
    home = True
    posts_all = BlogPost.objects.all()
    paginator = Paginator(posts_all, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts':posts,'home':home}
    return render(request,'post/index.html',context)

@login_required(login_url='signin')
def postDetails(request,slug):
    home = False
    posts = BlogPost.objects.all()
    post = get_object_or_404(posts,slug=slug)
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'post':post,
               'posts':posts,
               'home':home,
                'comments':comments,
                'new_comment':new_comment,
                'comment_form':comment_form}
    return render(request,'post/details.html',context)

def postAdd(request):
    home = False
    message = ''
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            img_object = form.instance 
            message = 'Félicitation l\'article a été bien crée.'
            context = {
                'img_obj':img_object,
                'message':message,
               'home':home,
                'form':form}
            return render(request,'post/add_post.html',context)
    else:
        form = PostForm()
    context = {
               'home':home,
                'form':form}
    return render(request,'post/add_post.html',context)

# update view for details
def postUpdate(request, slug):
    context ={}
    message = ''
    home=False
    posts = BlogPost.objects.all()
    obj = get_object_or_404(posts, slug=slug)
 
    form = PostForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        message = 'Félicitation l\'article a été bien modifié.'
        context = {
                'message':message,
               'home':home,}
        return render(request, "post/update_post.html", context)
 
    context["form"] = form
    return render(request, "post/update_post.html", context)

def postDelete(request, slug):
    posts = BlogPost.objects.all()
    post = get_object_or_404(posts, slug = slug)

    if request.method =="POST":
        post.delete()
        return redirect('dashboard')
    context ={'post':post}
 
    return render(request, "post/delete_post.html", context)
