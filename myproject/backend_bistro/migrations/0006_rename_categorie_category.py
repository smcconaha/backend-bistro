# Generated by Django 4.1.3 on 2022-11-10 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro', '0005_rename_category_categorie_alter_menu_item_cuisine_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
    ]
