# Generated by Django 4.1.3 on 2022-12-01 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapp.middleware.current_user


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(default=mainapp.middleware.current_user.CurrentUserMiddleware.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]