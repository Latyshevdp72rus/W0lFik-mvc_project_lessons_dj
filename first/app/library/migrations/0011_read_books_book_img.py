# Generated by Django 4.0.5 on 2022-07-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_extradition_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='read_books',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/%y/%m/%d/', verbose_name='Ссылка на изображение'),
        ),
    ]