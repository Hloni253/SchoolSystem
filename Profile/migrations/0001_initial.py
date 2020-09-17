# Generated by Django 3.0.3 on 2020-09-16 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0002_notes_topic_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ManyToManyField(blank=True, null=True, related_name='TeacherClasses', to='Courses.Class')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ManyToManyField(blank=True, null=True, related_name='StudentClasses', to='Courses.Class')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Courses.Course')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Profile.Profile')),
            ],
        ),
    ]
