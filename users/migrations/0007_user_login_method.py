# Generated by Django 3.2.6 on 2021-08-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210823_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('en', 'english'), ('kr', 'korean')], default='Email', max_length=50),
        ),
    ]
