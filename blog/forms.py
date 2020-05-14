from django import forms

from .models import Post, Comment

#имя для нашей формы, эта форма относится к ModelForm
class PostForm(forms.ModelForm):
    
#class Meta, где мы определяем, какая модель будет использоваться для создания формы (model = Post)
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)