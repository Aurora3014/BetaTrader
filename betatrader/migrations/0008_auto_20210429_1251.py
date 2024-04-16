# Generated by Django 3.1.6 on 2021-04-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betatrader', '0007_partner_totalsales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='totalEarned',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='totalSales',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='totalWithdraw',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
