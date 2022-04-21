from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import CommentForm, BlogForm


def blog(request):
    """ Post A Blog """
    blogs = Blog.objects.all()

    template = 'blog/blog.html'
    context = {
        'blogs': blogs,
    }

    return render(request, template, context)


def blog_detail(request, slug):
    """ Details on Blog Post """
    blog = Blog.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog
            obj.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """ Add a blog post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only our team has access to this.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added a blog post!')
            return redirect(reverse('blog_detail', args=[blog.slug]))
        else:
            messages.error(
                request, 'Failed to add the blog post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """ Edit a Blog Post """
    if not request.user.is_superuser:
        messages.error(request, 'Only our team has access to this.')
        return redirect(reverse('homepage'))

    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_detail', args=[blog.slug]))
        else:
            messages.error(
                request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """ Delete a blog post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only our team has access to this.')
        return redirect(reverse('homepage'))

    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('blog'))
