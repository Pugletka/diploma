from django.shortcuts import render

# Create your views here.
'''view, или представление, — это то место, где мы разместим «логику» работы нашего приложения. 
Оно запросит информацию из модели, которую мы создали ранее, и передаст её в шаблон'''

#функция с именем post_list, которая принимает request в качестве аргумента и возвращает результат 
#работы функции render, которая уже соберёт шаблон страницы
def post_list(request): 
    return render(request, 'blog/post_list.html', {})