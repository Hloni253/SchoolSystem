# Generated by Django 3.0.3 on 2020-09-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_notes_topic_notes'),
        ('Profile', '0002_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(blank=True, related_name='StudentClasses', to='Courses.Class'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(blank=True, related_name='TeacherClasses', to='Courses.Class'),
        ),
    ]
