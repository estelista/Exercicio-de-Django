from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="marca",
            field=models.CharField(default="Genérica", max_length=50),
        ),
    ]
