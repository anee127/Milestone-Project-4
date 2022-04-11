from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, null=False, blank=False)
    blog_author = models.TextField(max_length=100, null=False, blank=False)
    blog_content = models.TextField(null=False, blank=False)
    blog_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, null=False, blank=False, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True,)
    content = models.TextField(null=True, blank=True,)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment