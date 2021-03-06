from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class DatePublishedManager(models.Manager):
    """manager to get posts which are published"""

    def get_queryset(self):
        return super(DatePublishedManager, self).get_queryset().filter(status='published')

        #return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='date_published')
    body = models.TextField()
    author = models.ForeignKey(User, related_name='blog_posts')
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')

    # query manager
    objects = models.Manager()  # default manager
    published = DatePublishedManager() # published manager

    class Meta:
        ordering = ('-date_published',)

    def __str__(self):
        return self.title
