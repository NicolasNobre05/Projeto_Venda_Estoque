# Generated by Django 5.1.4 on 2024-12-31 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Cadastro', '0002_alter_cliente_numeroresidencial_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='CEP',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='CEP',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Estado',
            new_name='estado',
        ),
    ]
