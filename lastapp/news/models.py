from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Title', max_length=70, default='Something new')
    intro = models.CharField('Introduction', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
