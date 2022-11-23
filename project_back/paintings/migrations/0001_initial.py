
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, verbose_name='제목')),
                ('content', models.TextField(blank=True, max_length=200, verbose_name='내용')),
                ('before_image', models.ImageField(blank=True, upload_to='before_img', verbose_name='변환 전 사진')),
                ('after_image', models.ImageField(blank=True, upload_to='after_img', verbose_name='변환 후 사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시간')),
                ('style', models.CharField(choices=[('Composition_vii', '01_eccv16_composition_vii.t7'), ('La_muse(1)', '02_eccv16_la_muse.t7'), ('Starry_night(1)', '03_eccv16_starry_night.t7'), ('The_wave', '04_eccv16_the_wave.t7'), ('Candy', '05_instance_norm_candy.t7'), ('Feathers', '06_instance_norm_feathers.t7'), ('La_muse(2)', '07_instance_norm_la_muse.t7'), ('Mosaic', '08_instance_norm_mosaic.t7'), ('Starry_night(2)', '09_instance_norm_starry_night.t7'), ('The_scream', '10_instance_norm_the_scream.t7'), ('Udnie', '11_instance_norm_udnie.t7')], max_length=20, verbose_name='스타일')),
                ('is_auction', models.BooleanField(default=False, verbose_name='경매상태')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_painting', to=settings.AUTH_USER_MODEL, verbose_name='원작자')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owner_painting', to=settings.AUTH_USER_MODEL, verbose_name='소유자')),
            ],
            options={
                'db_table': 'db_painting',
            },
        ),
    ]
