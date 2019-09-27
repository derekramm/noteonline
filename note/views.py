from django.shortcuts import *

# Create your views here.
from note.forms import LoginForm, RegisterForm
from note.models import *
from note.utils.baidu_nlp_helper import *


def index(request):
    title = '首页'
    articles = Article.objects.all()
    return render(request, 'note/index.html', locals())


def login(request):
    title = '用户登录'
    if request.method == 'GET':
        return render(request, 'note/login.html', locals())
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            try:
                # author = Author.objects.get(username=username, password=password)
                author = Author.objects.get(**cd)
                request.session['author'] = author
                return redirect('note:index')
            except Author.DoesNotExist:
                error_message = '登录失败'
                return render_to_response('note/login.html', locals())
        return render(request, 'note/login.html', locals())


def sign_out(request):
    del request.session['author']
    return render(request, 'note/login.html', locals())


def register(request):
    title = '用户注册'
    if request.method == 'GET':
        return render(request, 'note/register.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        poster = request.FILES.get('poster')
        author = Author(username=username, password=password, email=email, poster=poster)
        author.save()
        request.session['author'] = author
        return render(request, 'note/index.html', locals())


def create(request):
    title = '新增文章'
    if request.method == 'GET':
        return render(request, 'note/create.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        summary = get_news_summary(content)
        created_at = timezone.now()
        updated_at = timezone.now()
        author = request.session['author']
        topics = get_topic(title, content)
        tags = get_keyword(title, content)
        Article.objects.create(
            title=title,
            content=content,
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            author=author,
            topics=topics,
            tags=tags
        )
        return redirect('note:index')


def detail(request, id):
    title = '文章明细'
    article = Article.objects.get(pk=id)
    return render(request, 'note/detail.html', locals())

