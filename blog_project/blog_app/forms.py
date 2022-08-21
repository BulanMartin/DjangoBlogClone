from django import forms
from blog_app.models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm

# Form for Post class
class PostForm(forms.ModelForm):

    class Meta():

        model = Post
        fields = ('author', 'title', 'text')

        # add styling to the form items
        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'author':forms.Select(attrs = {'class':'form-select form-select-lg mb-3'}),
            'text':forms.Textarea(attrs = {'class':'form-control','rows':'3'}),
        }

# Form for Comment class
class CommentForm(forms.ModelForm):

    class Meta():

        model = Comment
        fields = ('author', 'text')

        # add styling to the form items
        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea'})
        }

# Add css class to authentication form
class PrettyAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'input100',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
        })
    )
