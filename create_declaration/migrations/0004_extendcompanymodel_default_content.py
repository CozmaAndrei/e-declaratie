# Generated by Django 5.0.1 on 2024-03-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_declaration', '0003_alter_extendcompanymodel_pdf_declaration'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendcompanymodel',
            name='default_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
