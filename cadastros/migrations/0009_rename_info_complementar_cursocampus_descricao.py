# Generated by Django 4.0.5 on 2022-10-01 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_rename_descricao_cursocampus_info_complementar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursocampus',
            old_name='info_complementar',
            new_name='descricao',
        ),
    ]
