# Generated by Django 2.0.2 on 2018-02-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oai_pmh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('spec', models.TextField(unique=True, verbose_name='Spec')),
                ('name', models.TextField(verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
                'ordering': ('name',),
            },
        ),
    ]
