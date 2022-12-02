

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapp.middleware.current_user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodName', models.CharField(max_length=300)),
                ('Sodium_mg', models.SmallIntegerField(null=True)),
                ('Potassium_mg', models.SmallIntegerField(null=True)),
                ('Phosphate_mg', models.SmallIntegerField(null=True)),
                ('Protein_g', models.SmallIntegerField(null=True)),
                ('Water_L', models.SmallIntegerField(null=True)),
            ],
            options={
                'db_table': 'food_item',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Min_Sodium_mg', models.SmallIntegerField()),
                ('Max_Sodium_mg', models.SmallIntegerField()),
                ('Min_Potassium_mg', models.SmallIntegerField()),
                ('Max_Potassium_mg', models.SmallIntegerField()),
                ('Min_Phosphorous_mg', models.SmallIntegerField()),
                ('Max_Phosphorous_mg', models.SmallIntegerField()),
                ('Protein_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('M_Water_L', models.DecimalField(decimal_places=2, max_digits=5)),
                ('F_Water_L', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MealClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MealName', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'meal_class',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('HeightFt', models.SmallIntegerField()),
                ('HeightIn', models.SmallIntegerField()),
                ('Weight', models.SmallIntegerField()),
                ('Sex', models.CharField(max_length=20)),
                ('user', models.OneToOneField(default=mainapp.middleware.current_user.CurrentUserMiddleware.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='WaterEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.CharField(max_length=20)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.userinfo')),
            ],
            options={
                'db_table': 'water_entry',
            },
        ),
        migrations.CreateModel(
            name='FoodEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.CharField(max_length=20)),
                ('NumServings', models.DecimalField(decimal_places=2, max_digits=4)),
                ('FoodID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.fooditem')),
                ('MealName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.mealclass')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.userinfo')),
            ],
            options={
                'db_table': 'food_entry',
            },
        ),
        migrations.CreateModel(
            name='Actuals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Protein_g', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Water_L', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Sodium_mg', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Potassium_mg', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Phosphorous_mg', models.DecimalField(decimal_places=2, max_digits=8)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.userinfo')),
            ],
            options={
                'db_table': 'actuals',
            },
        ),
    ]
