from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author      = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title       = models.CharField(max_length = 200)
    text        = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())

    # editable (to be defined after the post is published)
    published_date = models.DateTimeField(blank = True, null = True)

    # publish post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # return list of approved comments
    def approve_comment(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    # define title to be returned by __str__ method
    def __str__(self):
        return self.title

class Comment(models.Model):

    # each post has its comments
    post             = models.ForeignKey('blog_app.Post',
                            related_name = 'comments',
                            on_delete=models.CASCADE)
    author           = models.CharField(max_length = 200)
    text             = models.TextField()
    create_date      = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)

    # set comment to approved
    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    # define text to be returned by __str__ method
    def __str__(self):
        return self.text
