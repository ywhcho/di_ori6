from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='ypri24',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='연생산액'),
        ),
    ]
