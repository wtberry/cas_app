# Generated by Django 2.1.2 on 2018-12-11 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('stu_id', models.AutoField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('schools', models.CharField(choices=[('UG', 'Undergraduate'), ('GD', 'graduate')], default='UG', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('courses', models.ManyToManyField(to='cas.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('finish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cas.Course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cas.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cas.Position')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('stu_id', models.AutoField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('schools', models.CharField(choices=[('UG', 'Undergraduate'), ('GD', 'graduate')], default='UG', max_length=2)),
                ('courses', models.ManyToManyField(to='cas.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='session',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cas.Tutor'),
        ),
        migrations.AddField(
            model_name='client',
            name='course',
            field=models.ManyToManyField(to='cas.Course'),
        ),
    ]
