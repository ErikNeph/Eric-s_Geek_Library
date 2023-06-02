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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения автора', null=True, verbose_name='Дата рождения автора')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смерти автора', null=True, verbose_name='Дата смерти автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=300, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1200, verbose_name='Аннотация книги')),
                ('isbn', models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выберете автора книги', null=True, to='catalog.Author', verbose_name='Автор книги')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=25, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус книги', max_length=20, verbose_name='Статус экзепляра книг')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер экземпляра', max_length=20, null=True, verbose_name='Инвентарьный номер')),
                ('imprint', models.CharField(help_text='Введите издательство и год выпуска', max_length=300, verbose_name='Издательство')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Status', verbose_name='Статус экземляра книги')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text=' Выберете жанр книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберете язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Language', verbose_name='Язык книги'),
        ),
    ]
