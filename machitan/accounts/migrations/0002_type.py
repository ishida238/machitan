# Generated by Django 3.2.16 on 2022-11-29 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=50, verbose_name='種類名')),
            ],
            options={
                'verbose_name_plural': 'Type',
            },
        ),
    ]
