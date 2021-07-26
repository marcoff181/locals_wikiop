# Generated by Django 3.2.5 on 2021-07-18 18:41

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('wikiop_api', '0008_auto_20210718_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionandanswer',
            name='primary_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question', to='wikiop_api.primarysection'),
        ),
        migrations.AlterField(
            model_name='questionandanswer',
            name='secondary_section',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='primary_section', chained_model_field='primary_section', on_delete=django.db.models.deletion.CASCADE, related_name='question', to='wikiop_api.secondarysection'),
        ),
    ]
