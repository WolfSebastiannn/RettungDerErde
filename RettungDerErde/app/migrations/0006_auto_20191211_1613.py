# Generated by Django 2.2.8 on 2019-12-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191204_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Netzwerke',
            new_name='poll',
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.BooleanField(verbose_name='Status'),
        ),
    ]
