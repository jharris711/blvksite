# Generated by Django 2.2.13 on 2020-06-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200611_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('embed', models.CharField(max_length=10000)),
            ],
        ),
    ]
