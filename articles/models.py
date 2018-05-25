from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(verbose_name="Загаловок", max_length=40, blank=True)
    text = models.TextField(verbose_name="Текст статьи", blank=True)
    image = models.ImageField(upload_to='static/img', blank=True)
    slug = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('articles:article',
                        args=[self.slug])
