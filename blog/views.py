from django.shortcuts import (
    render, reverse, redirect, get_object_or_404)
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def blog(request):
    blogs = Blog.objects.all()
    template = 'blog/blog.html'

    context = {
        'blog': blogs,
    }
    return render(request, template, context)


def blog_detail(request, blog_id):
    single_blog = get_object_or_404(Blog, pk=blog_id)
    blog_comments = Comment.objects.all()
    profile = None

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            initial_data = {
                'username': request.user,
                'email': profile.user.email,
            }
            form = CommentForm(initial=initial_data)
        except UserProfile.DoesNotExist:
            form = CommentForm()
    else:
        form = CommentForm()
    template = 'blog/blog_detail.html'
    if request.method == "POST":

        form_data = {
                    'comments': request.POST['comments'],
                }

    form = CommentForm(form_data)
    if form.is_valid():
            comment = form.save(commit=False)
            comment.Blog_id = blog_id
            comment.username = request.POST['username']
            comment.email = request.POST['email']
            comment.save()
            messages.success(request, 'New Blog content Added Successfully !')
            return redirect(reverse('blog_detail', args=(blog.id,)))
    else:
        messages.error(
            request, 'Failed to add comment. Please ensure that the form is valid')

    context = {
        'blog': single_blog,
        'form': form,
        'comments': comments,
    }
    return render(request, template, context)

@login_required()
def add_blog(request):
    if request.method == 'POST':
        form_data = {
                'blog_title': request.POST['blog_title'],
                'blog_author': request.POST['blog_author'],
                'blog_content': request.POST['blog_content'],
            }
        blog_form = BlogForm(form_data)
        if blog_form.is_valid():
            blog = blog_form.save()
            messages.success(request, 'New Blog content Added Successfully!')
            return redirect(reverse('blog_detail', args=(blog.id)))
        else:
            messages.error(request, 'Failed to add Blog post. Please ensure the form is valid')
    else:
        blog_form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Successfully updated Blog!')
            return redirect(reverse('blog_detail', args=(blog.id)))
        else:
            messages.error(request, 'Failed to update Blog. Please ensure the form is valid.')
    else:
        blog_form = BlogForm(instance=blog)
    messages.info(request, f'You are editing {blog.blog_title}')
    template = 'blog/edit_blog.html'

    context = {
        'blog_form': blog_form,
        'blog': blog,
    }
    return render(request, template, context)

@login_required
def delete_blog(request, blog_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only Administrator can do that')
        return redirect(reverse('home'))    
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog Deleted!')

    return redirect(reverse('blog'))    
