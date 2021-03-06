# Generated by Django 3.1.7 on 2021-03-10 18:25. Formatted by Black

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grants", "0004_auto_20210310_1818"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grant",
            name="advance_allowed_ind",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No")],
                max_length=1,
                null=True,
                verbose_name="Advance Allowed",
            ),
        ),
    ]
