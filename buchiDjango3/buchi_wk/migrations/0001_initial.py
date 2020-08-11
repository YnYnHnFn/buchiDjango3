# Generated by Django 3.0 on 2020-08-11 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuchiMdl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fld_Char', models.CharField(max_length=10)),
                ('fld_Text', models.TextField()),
                ('fld_URL', models.URLField()),
                ('fld_Email', models.EmailField(max_length=254)),
                ('fld_Slug', models.SlugField()),
                ('fld_FilePath', models.FilePathField(path='C:\\Users\\buchi\\source\\repos\\buchiDjango3\\buchiDjango3/local_files')),
                ('fld_GenericIPAddress', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('fld_Integer', models.IntegerField()),
                ('fld_SmallInteger', models.SmallIntegerField()),
                ('fld_PositiveInteger', models.PositiveIntegerField()),
                ('fld_PositiveSmallInteger', models.PositiveSmallIntegerField()),
                ('fld_BigInteger', models.BigIntegerField()),
                ('fld_Decimal', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fld_Float', models.FloatField()),
                ('fld_Date', models.DateField()),
                ('fld_DateTime', models.DateTimeField()),
                ('fld_Time', models.TimeField()),
                ('fld_Duration', models.DurationField(verbose_name='holds the time period')),
                ('fld_Binary', models.BinaryField()),
                ('fld_File', models.FileField(upload_to='C:\\Users\\buchi\\source\\repos\\buchiDjango3\\buchiDjango3/local_files', verbose_name='File upload fields')),
                ('fld_Boolean', models.BooleanField()),
                ('fld_NullBoolean', models.NullBooleanField()),
            ],
        ),
    ]
