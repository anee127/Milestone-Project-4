from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['blog_title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-product-form-field'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Comment"
