# Generated by Django 4.1.2 on 2022-12-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_user_userinfo_alter_fooditem_phosphate_mg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodentry',
            name='DateTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='waterentry',
            name='DateTime',
            field=models.CharField(max_length=20),
        ),
    ]
