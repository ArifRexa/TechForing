# Generated by Django 5.1.4 on 2024-12-27 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_hints_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp_expiration',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp_resend_attempts',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp_resend_cooldown_period',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp_resend_last_attempt',
        ),
    ]
