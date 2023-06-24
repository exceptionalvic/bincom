# Generated by Django 3.2 on 2023-06-24 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentName',
            fields=[
                ('name_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('pollingunit_uniqueid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Announced_LGA_Results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Announced_PU_Results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('polling_unit_uniqueid', models.IntegerField(null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Announced_State_Results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Announced_Ward_Results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField()),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.IntegerField()),
                ('lga_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyid', models.CharField(max_length=11)),
                ('partyname', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Polling_Unit',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField(blank=True, null=True)),
                ('polling_unit_number', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_description', models.TextField()),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
                ('entered_by_user', models.CharField(blank=True, max_length=50, null=True)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField()),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_id', models.IntegerField()),
                ('ward_name', models.CharField(max_length=50)),
                ('lga_id', models.IntegerField()),
                ('ward_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FilterPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec.lga')),
                ('pu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec.polling_unit')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec.ward')),
            ],
        ),
    ]