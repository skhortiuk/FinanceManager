# Generated by Django 2.1.4 on 2019-01-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20190104_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_added',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
