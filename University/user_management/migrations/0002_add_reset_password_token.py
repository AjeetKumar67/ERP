from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reset_password_token',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
