

# django

장고를 활용해서 게시판 CRUD기능을 구현하는 실습을 진행하여 학습할 예정입니다.

 

## Get Started

### 프로젝트 생성

현재 디렉토리에서 practice라는 프로젝트를 생성합니다.

```
$ django-admin startproject practice
```

```
practice/
    manage.py
    practice/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```



### 게시판 앱 생성

1. 게시판 앱을 생성합니다.

```
$ python manage.py startapp articles
```

```
practice/
    manage.py
    practice/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    articles/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```



2. 게시판 앱을 practice/settings.py 에 등록해줍니다.

```pyhton
INSTALLED_APPS = [
    # app
    "articles", #생성된 앱을 추가해줍니다.

    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```



### 앱 분리

프로젝트가 확장성을 위해서 프로젝트의 url을 분리하는 작업을 진행합니다.

1. /practice/url.py

```
from django.contrib import admin
from django.urls import path, include


# 확장성 및 가독성을 위해 url 분리
# 각 App에 대해 include 사용

urlpatterns = [
    path("admin/", admin.site.urls),
    parth("articles/", include("articles.urls")),
]
```

2. /articles/urls.py

   앱 내 urls.py을 생성하여 앱 별로 url을 관리합니다.
   효율적인 url 관리를 위해서 url 마다 name을 지정해줍니다.
   또한 다른 앱과 url이름이 겹치는 문제를 방지하기 위해 namespace를 추가합니다.

```
from django.contrib import admin
from django.urls import path
from . import views

# articles/urls.py app 내의 url.py
app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
]
```

```
<a href="{% url 'articles:index' %}"> main </a>
```



### Views

```
```

충돌을 막기 위해 templates/articles 디렉토리 내 index.html 생성

```html
```



## Model

```
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
		
```



## Model Queryset

1. Create

```python
# 방법 1
article = Article() 
article.title = "글1"
article.content = "내용1"
article.save()

# 방법 2
article = Article(title=“글1”, content=“내용1”) 
article.save()

# 방법 3
Article.objects.create(title=“글1", content="내용1")
```

2. Read

```
In [1]: Article.objects.get(pk=1)
Out[1]: <Article: Article object (1)>
```

3. Update

```
In [1]: article = Article.objects.get(pk=1)
In [2]: article.title = "글2"
In [3]: article.save()
```

4. Delete

```
In [1]: article = Article.objects.get(pk=1)
In [2]: article.delete()
Out[2]: (1, {'articles.Article': 1})
```





## admin

```
$ python manage.py createsuperuser

사용자 이름 (leave blank to use '사용자 이름'): admin
이메일 주소:               
Password: 
Password (again): 
Superuser created successfully.
```

