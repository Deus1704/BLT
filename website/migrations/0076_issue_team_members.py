# Generated by Django 4.1 on 2023-06-30 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0075_company_logo_issue_rewarded_alter_company_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='team_members',
            field=models.ManyToManyField(related_name='reportmembers', to=settings.AUTH_USER_MODEL),
        ),
    ]
