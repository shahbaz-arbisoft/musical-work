from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=300, help_text='Work Title', verbose_name='Work Title')
    ISWC = models.CharField(max_length=250, unique=True, db_index=True,
                            help_text='International Standard Musical Work Code',
                            verbose_name='International Standard Musical Work Code')
    contributors = models.ManyToManyField('Contributor', related_name='contributors', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Works"

    def __str__(self):
        return self.title


class Contributor(models.Model):
    name = models.CharField(max_length=300, help_text='Contributor Name', verbose_name='Contributor Name')

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Contributors"

    def __str__(self):
        return self.name
