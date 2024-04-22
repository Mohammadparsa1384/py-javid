# Generated by Django 5.0.3 on 2024-03-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='توضیحات'),
        ),
    ]