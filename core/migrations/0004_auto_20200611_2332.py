# Generated by Django 2.2.13 on 2020-06-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_about_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='post',
            new_name='paragraph_one',
        ),
        migrations.AddField(
            model_name='about',
            name='paragraph_two',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
