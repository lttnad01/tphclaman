# Generated by Django 4.0.6 on 2022-07-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nghang', '0012_intro_mymap_alter_intro_address_alter_intro_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=200, verbose_name='Tiêu đề bài viết')),
                ('postcontent', models.TextField(verbose_name='Nội dung bài viết')),
            ],
            options={
                'verbose_name': 'Tin tức',
                'verbose_name_plural': 'Tin tức',
            },
        ),
        migrations.AlterField(
            model_name='intro',
            name='mymap',
            field=models.CharField(max_length=500, verbose_name='Google Map'),
        ),
    ]
