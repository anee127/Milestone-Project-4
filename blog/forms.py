""" forms for blog """
from django import forms
from .models import Comment
from .models import Blog


class CommentForm(forms.ModelForm):
    """ comments form """
    class Meta:
        """ meta class for comments model """
        model = Comment
        fields = ['name', 'statement']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['statement'].label = "Comment"


class BlogForm(forms.ModelForm):
    """ blogs form """
    class Meta:
        """ meta class for blog model """
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-product-form-field'
