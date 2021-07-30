from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import PostForm
from blog.models import Post


def index(request):  # HttpRequest의 객체가 request 요청
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)

    #return HttpResponse("블로그 메인 페이지입니다.")  # 응답

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)

def detail(request, post_id):
    #post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
