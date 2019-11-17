# Generated by Django 2.2.7 on 2019-11-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_member_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='groups',
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='groups.Member'),
        ),
    ]