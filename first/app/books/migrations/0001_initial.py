# Generated by Django 4.0.5 on 2022-06-13 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('father_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Отчество')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('birthday', models.DateField(max_length=8, verbose_name='Дата рождения')),
                ('languages', models.JSONField(blank=True, null=True, verbose_name='Язык на котором пишет автор')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='удалено')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_house_name', models.CharField(max_length=300, verbose_name='Название издательство')),
                ('pub_house_address', models.CharField(max_length=1500, verbose_name='Адрес издательства')),
                ('pub_house_contact_phone', models.CharField(max_length=20, verbose_name='Номер телефона издательства')),
                ('pub_house_email', models.EmailField(max_length=254, verbose_name='Название почты издательства')),
                ('pub_house_site', models.URLField(blank=True, null=True, verbose_name='Сайт издательства')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='удалено')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('date_creation', models.DateTimeField(verbose_name='Дата написании книги')),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('is_daleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('author', models.ManyToManyField(to='books.author')),
                ('id_publishing_house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publishinghouse_books', to='books.publishinghouse', verbose_name='ID Издательства')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]