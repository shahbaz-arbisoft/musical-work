# Generated by Django 4.0.3 on 2022-04-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Contributor Name', max_length=300, verbose_name='Contributor Name')),
            ],
            options={
                'verbose_name_plural': 'Contributors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Work Title', max_length=300, verbose_name='Work Title')),
                ('ISWC', models.CharField(help_text='International Standard Musical Work Code', max_length=250, verbose_name='International Standard Musical Work Code')),
                ('contributors', models.ManyToManyField(related_name='contributors', to='musicalapp.contributor')),
            ],
            options={
                'verbose_name_plural': 'Works',
                'ordering': ['title'],
            },
        ),
    ]
