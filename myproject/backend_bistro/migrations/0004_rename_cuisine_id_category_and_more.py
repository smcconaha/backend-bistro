# Generated by Django 4.1.3 on 2022-11-09 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro', '0003_alter_category_id_id_alter_cuisine_id_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuisine_id',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Category_id',
            new_name='Cuisine',
        ),
    ]
