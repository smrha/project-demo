from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='p')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'انتشار یافته')
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    author = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                args=[self.publish.year,
                    self.publish.month,
                    self.publish.day,
                    self.slug])

    # Return fullname of post author
    def get_author(self):
        return f"{self.author.first_name} {self.author.last_name}"

