from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView,
                    DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from blog_app.forms import PostForm, CommentForm, PrettyAuthenticationForm
from blog_app.models import Post, Comment
from django.contrib.auth.views import LoginView


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # Get posts in descending order
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

    # Inherit LoginRequiredMixin for authorization
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

    # Inherit LoginRequiredMixin for authorization
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

    # Inherit LoginRequiredMixin for authorization
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

    # Show all posts in draft
class DraftListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    success_url = reverse_lazy('post_list')

    # Get posts in descending order
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('create_date')

class CustomLoginView(LoginView):

    #template_name = 'blog_app/about.html'
    authentication_form = PrettyAuthenticationForm
    print('abcd')

###################################################################

# publish new post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('post_detail', pk = pk)

# add unapproved comment, return to corresponding post detail page
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog_app/comment_form.html', {'form':form})

# approve unapproved comment, return to corresponding post detail page
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)

# remove comment, return to corresponding post detail page
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)
