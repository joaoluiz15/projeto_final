# Generated by Django 4.2.3 on 2023-12-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_carro_cpf_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='cpf_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.cliente'),
        ),
    ]
