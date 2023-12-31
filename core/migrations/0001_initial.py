# Generated by Django 4.1.10 on 2023-09-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(default='', max_length=90)),
                ('intensity', models.IntegerField(blank=True, default=0, null=True)),
                ('sector', models.CharField(default='', max_length=190)),
                ('topic', models.CharField(default='', max_length=70)),
                ('insight', models.CharField(default='', max_length=90)),
                ('url', models.CharField(default='', max_length=500)),
                ('region', models.CharField(default='', max_length=200)),
                ('start_year', models.CharField(default='', max_length=120)),
                ('impact', models.CharField(default='', max_length=120)),
                ('added', models.CharField(default='', max_length=500)),
                ('published', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('relevance', models.IntegerField(blank=True, default=0, null=True)),
                ('pestle', models.CharField(default='', max_length=190)),
                ('source', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=500)),
                ('likelihood', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
