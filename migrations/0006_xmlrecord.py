# Generated by Django 3.1.8 on 2021-04-06 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oai_pmh', '0005_oaidc_metadataformat'),
    ]

    operations = [
        migrations.CreateModel(
            name='XMLRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('xml_metadata', models.TextField(verbose_name='XML metadta')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xmlrecords', to='oai_pmh.header', verbose_name='Header')),
                ('metadata_prefix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xmlrecords', to='oai_pmh.metadataformat', verbose_name='Metadata prefix')),
            ],
            options={
                'verbose_name': 'XML record',
                'verbose_name_plural': 'XML records',
                'ordering': ('header', 'metadata_prefix'),
            },
        ),
    ]
