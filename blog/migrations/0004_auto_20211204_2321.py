# Generated by Django 3.1.13 on 2021-12-04 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211204_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audit',
            old_name='parents_email',
            new_name='guardian_email',
        ),
        migrations.RenameField(
            model_name='audit',
            old_name='parents_name',
            new_name='guardian_name',
        ),
        migrations.RenameField(
            model_name='audit',
            old_name='parents_phone_number',
            new_name='guardian_phone_number',
        ),
        migrations.AlterField(
            model_name='audit',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='auditionpic'),
        ),
    ]
