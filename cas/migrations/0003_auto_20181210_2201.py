# Generated by Django 2.1.2 on 2018-12-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas', '0002_auto_20181210_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='signiture',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(default='na', max_length=5),
            preserve_default=False,
        ),
    ]
