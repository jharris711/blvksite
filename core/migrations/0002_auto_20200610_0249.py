# Generated by Django 2.2.13 on 2020-06-10 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soundcloud',
            options={'ordering': ['-id']},
        ),
    ]