# Generated by Django 2.2.13 on 2020-06-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200621_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagram',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='instagram',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
