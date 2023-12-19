# Generated by Django 4.2.7 on 2023-12-19 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_selectfechas_remove_contacto_se_envio_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genealogista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('pais', models.CharField(max_length=50, verbose_name='pais')),
                ('ciudad', models.CharField(max_length=50, verbose_name='ciudad')),
                ('sitio_web', models.CharField(default='website', max_length=100, verbose_name='sitio web')),
                ('nombre_genealogista', models.CharField(max_length=16, verbose_name='nombre_genealogista')),
                ('logo_genealogista', models.ImageField(null=True, upload_to='imagenes/', verbose_name='logo genealogista')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('pais', models.CharField(max_length=50, verbose_name='pais')),
                ('ciudad', models.CharField(max_length=50, verbose_name='ciudad')),
                ('sitio_web', models.CharField(default='website', max_length=100, verbose_name='sitio web')),
                ('nombre_gestoria', models.CharField(max_length=16, verbose_name='nombre_gestoria')),
                ('logo_gestoria', models.ImageField(null=True, upload_to='imagenes/', verbose_name='logo gestor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo_de_consulta',
            field=models.IntegerField(choices=[('', '-Seleccione-'), (1, 'Informacion sobre gestión'), (2, 'Tengo problemas con el portal')], verbose_name='Tipo de consulta'),
        ),
    ]
