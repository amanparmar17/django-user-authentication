# Generated by Django 2.1.1 on 2019-01-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('enrollment', models.IntegerField(default=0)),
            ],
        ),
    ]
