# Generated by Django 4.2.6 on 2023-10-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_chain', '0002_alter_contacts_options_alter_link_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Задолженность'),
        ),
    ]