# Generated by Django 4.1.7 on 2023-02-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('curso', models.CharField(max_length=30)),
            ],
        ),
    ]
