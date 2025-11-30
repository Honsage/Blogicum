from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Location(PublishedModel):
    name = models.CharField(max_length=256)


class Post(PublishedModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
