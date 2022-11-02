# Generated by Django 4.1.2 on 2022-10-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_items_claimed_items_on_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsOnBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_descr', models.CharField(max_length=255)),
                ('item_picture', models.CharField(max_length=255)),
                ('highest_bid', models.IntegerField()),
                ('highest_bidder_username', models.CharField(max_length=255)),
                ('owner_username', models.CharField(max_length=255)),
                ('valid', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Items_claimed',
            new_name='ItemsClaimed',
        ),
        migrations.DeleteModel(
            name='Items_on_bid',
        ),
    ]
