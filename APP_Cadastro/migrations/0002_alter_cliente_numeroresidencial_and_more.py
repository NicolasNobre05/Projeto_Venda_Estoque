# Generated by Django 5.1.4 on 2024-12-31 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numeroResidencial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='numeroResidencial',
            field=models.CharField(max_length=100, null=True),
        ),
    ]