# Generated by Django 3.0.3 on 2020-09-15 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InheritFrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('inheritfrom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Courses.InheritFrom')),
            ],
            bases=('Courses.inheritfrom',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('inheritfrom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Courses.InheritFrom')),
            ],
            bases=('Courses.inheritfrom',),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('inheritfrom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Courses.InheritFrom')),
                ('topic_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Class', to='Courses.Class')),
            ],
            bases=('Courses.inheritfrom',),
        ),
        migrations.AddField(
            model_name='class',
            name='class_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Course', to='Courses.Course'),
        ),
    ]
