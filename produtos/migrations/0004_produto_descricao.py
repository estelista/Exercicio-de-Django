from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0003_produto_estoque"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="descricao",
            field=models.TextField(blank=True, null=True),
        ),
    ]
