# Generated by Django 3.2.5 on 2021-07-19 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wikiop_api', '0009_auto_20210718_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondarysection',
            name='primary_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondary_section', to='wikiop_api.primarysection'),
        ),
    ]