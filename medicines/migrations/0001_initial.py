from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htname', models.CharField(max_length=200, verbose_name='약품명')),
                ('ingr_t', models.CharField(max_length=1000, verbose_name='성분명')),
                ('e2iact_t', models.CharField(max_length=1000, verbose_name='성분함량')),
                ('ee', models.TextField(blank=True, verbose_name='효능')),
                ('company', models.CharField(max_length=200, verbose_name='회사명')),
                ('wfco', models.CharField(blank=True, db_index=True, default='', max_length=10, verbose_name='주성분코드')),
            ],
            options={
                'verbose_name': '의약품',
                'verbose_name_plural': '의약품 목록',
                'ordering': ['htname'],
            },
        ),
        migrations.CreateModel(
            name='DrugInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htname', models.CharField(max_length=200, verbose_name='약품명')),
                ('ingr_t', models.CharField(max_length=1000, verbose_name='성분명')),
                ('ee', models.TextField(blank=True, verbose_name='효능')),
                ('ud', models.TextField(blank=True, verbose_name='용량')),
                ('nb', models.TextField(blank=True, verbose_name='주의사항')),
                ('company', models.CharField(max_length=200, verbose_name='회사명')),
            ],
            options={
                'verbose_name': '의약정보',
                'verbose_name_plural': '의약정보 목록',
                'ordering': ['htname'],
            },
        ),
    ]
