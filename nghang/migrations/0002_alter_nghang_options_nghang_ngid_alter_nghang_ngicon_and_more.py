# Generated by Django 4.0.6 on 2022-07-20 02:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nghang', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nghang',
            options={'verbose_name': 'Ngành hàng', 'verbose_name_plural': 'Ngành hàng'},
        ),
        migrations.AddField(
            model_name='nghang',
            name='ngID',
            field=models.IntegerField(blank=True, null=True, verbose_name='STT'),
        ),
        migrations.AlterField(
            model_name='nghang',
            name='ngicon',
            field=models.ImageField(upload_to='img01/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='nghang',
            name='ngname',
            field=models.CharField(max_length=100, verbose_name='Tên ngành hàng'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prname', models.CharField(max_length=100, verbose_name='Tên sản phẩm')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Giá tiền')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('prcontent', models.CharField(max_length=100, verbose_name='Nội dung')),
                ('primage', models.ImageField(upload_to='imgProduct/', verbose_name='Ảnh sản phẩm')),
                ('nghang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lk_nghang', to='nghang.nghang')),
            ],
            options={
                'verbose_name': 'Sản phẩm',
                'verbose_name_plural': 'Sản phẩm',
            },
        ),
    ]
