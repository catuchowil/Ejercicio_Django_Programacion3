# Generated by Django 3.0 on 2020-09-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categorias'},
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre Producto')),
                ('pre_uni', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio Unitario')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Categoria', verbose_name='Categoria Producto')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'ordering': ['name'],
            },
        ),
    ]