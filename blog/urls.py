from django.urls import path
from . import views 
#импорт всех views (представления) из приложения blog

''' Как ты можешь заметить, мы связали view под именем post_list с корневым URL-адресом (''). 
Этот шаблон URL будет соответствовать пустой строке. Это правильно, потому что для обработчиков URL 
в Django 'http://127.0.0.1:8000/' не является частью URL. Этот шаблон скажет Django, что views.post_list — 
это правильное направление для запроса к твоему веб-сайту по адресу 'http://127.0.0.1:8000/'.
Последняя часть name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его. 
Оно может быть таким же, как имя представления (англ. view), а может и чем-то совершенно другим. Мы будем 
использовать именованные URL позднее в проекте, поэтому важно указывать их имена уже сейчас. Мы также 
должны попытаться сохранить имена URL-адресов уникальными и легко запоминающимися.'''

#URL-шаблон:
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]

'''Фрагмент post/<int:pk>/ определяет шаблон URL-адреса. Сейчас мы его поясним:
post/ значит, что после начала строки URL должен содержать слово post и косую черту /. Пока всё в порядке.
<int:pk> — эта часть посложнее. Она означает, что Django ожидает целочисленное значение и преобразует его в представление 
— переменную pk.
/ — затем нам нужен еще один символ / перед тем, как адрес закончится.'''