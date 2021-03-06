from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.published.all()

    return render(request, 'ogblog/post/list.html', {'posts': posts})

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             published__year=year,
                             publshed_month=month,
                             published_day=day)

    return render(request, 'ogblog/post/detail.html', {'post':post})
