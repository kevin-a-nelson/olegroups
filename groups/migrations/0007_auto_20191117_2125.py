# Generated by Django 2.2.7 on 2019-11-17 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_auto_20191117_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='default@stolaf.edu', max_length=254)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='group',
            name='title',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='member',
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='groups.Membership', to='groups.Person'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Person'),
            preserve_default=False,
        ),
    ]
