# Generated by Django 4.2.2 on 2023-09-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0003_rename_link_bild_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bild',
            name='img',
            field=models.ImageField(upload_to='img_trees/'),
        ),
    ]
