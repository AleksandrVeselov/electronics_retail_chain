# Generated by Django 4.2.6 on 2023-10-08 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail_chain', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'Звено', 'verbose_name_plural': 'Звенья'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
