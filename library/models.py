from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.contrib.auth import get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL
#User = get_user_model()

GENRE_CHOICES = (
    ('horror','HORROR'),
    ('mystery', 'MYSTERY'),
    ('thriller','THRILLER'),
    ('fiction','FICTION'),
    ('romantic','ROMANTIC'),
    ('motivational','MOTIVATIONAL'),
)

##add updated query set to the manager
class AuthorManager(models.Manager):
    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def annotate_with_copies_sold(self):
        return self.get_queryset().annotate_with_copies_sold()
#However you will no be able to use it on QuerySet object like:
#author_books = Author.objects.filter(id=2).total_copies_sold()

#That is because you are annotating Author object, not a QuerySet. To obtain that result you should execute:
# Author.objects.annotate_with_copies_sold().get(id=2)
# author.copies_sold 
# 15

##add anotate to queryset model
class AuthorQuerySet(models.QuerySet):
    def annotate_with_copies_sold(self):
        return self.annotate(copies_sold=Coalesce(Sum('books__copies_sold'),0))

class Author(models.Model):
    objects = AuthorManager()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '{a} {b}'.format(a = self.first_name, b = self.last_name)

class Book(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    copies_sold = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='fiction')

    def __str__(self):
        return self.title