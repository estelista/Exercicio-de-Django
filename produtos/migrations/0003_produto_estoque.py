from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0002_produto_marca"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="estoque",
            field=models.IntegerField(default=0),
        ),
    ]
