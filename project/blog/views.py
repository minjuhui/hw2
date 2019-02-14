from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog


def home(request):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs':blogs})    

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

# new.html 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog=Blog()     # 객체 생성
    blog.title=request.GET['title']     # form에서 임력한 내용
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save() # 메소드 중 하나 : 객채를 데이터베이스에 저장하라
    # redirect import
    # url은 항상 str
    return redirect('/blog/'+str(blog.id))

    # redirect와 render의 차이
    # redirect(url(다른 url 사용가능),)

### blog.id vs. blog_id 차이점 숙지하기
    