# Generated by Django 4.2.2 on 2023-10-20 15:35

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0009_alter_bild_img_alter_bild_pvnlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bild',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\\\Users\\\\marti\\\\Desktop\\\\Django\\\\trees_db_Project\\\\media\\\\/img_trees/'), upload_to=''),
        ),
    ]
