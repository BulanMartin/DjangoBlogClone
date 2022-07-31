from django import forms
from blog.models import Post, Comment

# Form for Post class
class PostForm(forms.ModelForm):

    class Meta():

        model = Post
        fields = ('author', 'title', 'text')

        # add styling to the form items
        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.TextArea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }

# Form for Comment class
class CommentForm(forms.ModelForm)

    class Meta():

        model = Comment
        fields = ('author', 'text')

        # add styling to the form items
        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.TextArea(attrs = {'class':'editable medium-editor-textarea'})
        }
