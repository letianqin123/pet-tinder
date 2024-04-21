# Generated by Django 4.0.6 on 2024-04-09 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_slug'),
        ('pet', '0007_alter_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='category.category'),
        ),
    ]
