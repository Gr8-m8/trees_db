# Generated by Django 4.2.2 on 2023-09-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0004_alter_bild_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bild',
            name='img',
            field=models.ImageField(upload_to='static/img_trees/'),
        ),
    ]