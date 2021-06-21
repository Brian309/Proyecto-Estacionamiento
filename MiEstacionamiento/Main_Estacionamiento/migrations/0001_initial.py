# Generated by Django 3.2.4 on 2021-06-21 04:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.UUIDField(default=uuid.uuid4, help_text='Id del vehiculo', primary_key=True, serialize=False)),
                ('patente', models.CharField(help_text='Ingrese la patente de su automovil', max_length=8)),
                ('marca', models.CharField(help_text='Ingrese la marca de su automovil', max_length=8)),
                ('color', models.CharField(help_text='ingrese el color del vehiculo', max_length=8)),
                ('año', models.CharField(help_text='Ingrese el año de su vehiculo', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, help_text='Id del usuario (Se crea solo)', primary_key=True, serialize=False)),
                ('rut_user', models.CharField(help_text='Indique su rut', max_length=10)),
                ('nom_user', models.CharField(help_text='Indique su Nombre', max_length=30)),
                ('password', models.CharField(help_text='Indique su contraseña', max_length=16)),
                ('email', models.EmailField(error_messages={'Error': 'Digite un formato de correo valido'}, help_text='Indique su Email', max_length=50)),
                ('vehiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main_Estacionamiento.vehiculo')),
            ],
        ),
    ]
