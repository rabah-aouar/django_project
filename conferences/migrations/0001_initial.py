# Generated by Django 3.1.7 on 2022-03-19 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=600)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('applied_personnes', models.ManyToManyField(related_name='conference_applied_personnes', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conference_creator', to=settings.AUTH_USER_MODEL)),
                ('reviewers', models.ManyToManyField(related_name='conference_reviewers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]