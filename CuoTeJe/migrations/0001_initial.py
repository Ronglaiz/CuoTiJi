# Generated by Django 4.1.4 on 2023-02-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemNo', models.IntegerField()),
                ('CorrectAnswer', models.CharField(max_length=2)),
                ('ItemDesc', models.CharField(max_length=3000)),
            ],
        ),
    ]
