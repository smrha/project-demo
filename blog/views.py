from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post/list.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
            status = 'p',
            publish__year=year,
            publish__month=month,
            publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                    f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'lord.smrha@gmail.com', cd['to'])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'form': form,
        'post': post,
        'sent': sent
    }
    return render(request, 'blog/post/share.html', context)
