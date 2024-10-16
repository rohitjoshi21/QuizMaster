# Generated by Django 5.1.2 on 2024-10-15 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('users', '0002_alter_organizationuser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.AddField(
            model_name='question',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='users.organizationuser'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(null=True, to='dashboard.question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='users.organizationuser'),
        ),
    ]
