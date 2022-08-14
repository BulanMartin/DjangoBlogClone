from django import forms
from blog_app.models import Post, Comment

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
