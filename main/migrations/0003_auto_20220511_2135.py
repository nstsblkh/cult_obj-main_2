# Generated by Django 3.2.6 on 2022-05-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220511_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultureobject',
            name='addresses',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='cultureobject',
            name='ensemble_name_on_doc',
            field=models.TextField(verbose_name='Название объекта в документах'),
        ),
        migrations.AlterField(
            model_name='cultureobject',
            name='location',
            field=models.TextField(verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='cultureobject',
            name='name',
            field=models.TextField(verbose_name='Название объекта'),
        ),
    ]