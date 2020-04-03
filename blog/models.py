from django.db import models
from django.utils import timezone
from django.conf import settings

#эта строка определяет нашу модель (объект), Post — это имя нашей модели
#models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title