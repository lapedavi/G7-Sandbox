# Generated by Django 4.2 on 2023-04-15 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CollectAll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='CollectAll.collection'),
        ),
    ]
