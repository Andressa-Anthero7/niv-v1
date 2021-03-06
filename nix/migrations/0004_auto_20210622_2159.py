# Generated by Django 3.2.4 on 2021-06-23 00:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0003_rename_modelo_veiculo_anuncio_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='imagens/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
