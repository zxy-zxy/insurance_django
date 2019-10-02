from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('insurance_api', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('type', models.CharField(max_length=255)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cover', models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    'customer',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='policies',
                        to='insurance_api.Customer',
                    ),
                ),
            ],
        )
    ]
