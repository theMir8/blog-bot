# Generated by Django 3.2.4 on 2021-06-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210606_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users registered in the bot'},
        ),
        migrations.AlterField(
            model_name='botuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='User is active?'),
        ),
    ]