# Generated by Django 3.0.8 on 2020-07-03 21:30

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
    ]
