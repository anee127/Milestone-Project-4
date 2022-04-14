from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    statement = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.blog.title, self.name)     
