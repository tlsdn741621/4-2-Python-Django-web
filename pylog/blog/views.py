from django.shortcuts import render, redirect
from rest_framework import viewsets

from blog.models import Post, Comment
from blog.serializers import PostSerializer


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html',context)

def post_detail(request,post_id):
    print("화면에서 전달 받은 상세 페이지 게시글 번호 post_id :", post_id)
    post = Post.objects.get(id=post_id)
    print(post)
    # 추가, 상세보기 화면에서, post로 들어 올경우, 댓글 콘솔에 확인 해보기.
    if request.method == 'POST':
        comment_content = request.POST["comment"]
        print(comment_content)
        Comment.objects.create(
            post=post,
            content=comment_content
        )
    context = {
        # "post_id": post_id,
        "post": post
    }
    return render(request, 'post_detail.html',context)

# 1) 글 작성 화면,GET 2) 글 로직 처리,POST
def post_add(request):
    if request.method == 'POST':
        # 추가
        print(request.FILES)
        title = request.POST['title']
        content = request.POST['content']
        print(title)
        print(content)
        # 추가
        thumbnail = request.FILES['thumbnail']
        # 추가
        post = Post.objects.create(
            title=title,
            content=content,
            # 추가
            thumbnail=thumbnail
        )
        return redirect(f'/posts/{post.id}')
    else:
        print("method GET")
    return render(request, 'post_add.html')

class PostViewSet(viewsets.ModelViewSet):
    """
    Post 모델에 대한 CRUD API를 제공하는 ViewSet
    """
    queryset = Post.objects.all() # 모든 Post 객체를 가져와 최신순으로 정렬
    serializer_class = PostSerializer