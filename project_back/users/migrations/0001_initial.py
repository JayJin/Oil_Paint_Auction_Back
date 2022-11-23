from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': '이미 사용중인 이메일 이거나 탈퇴한 이메일 입니다.'}, max_length=100, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(error_messages={'unique': '이미 사용중인 닉네임 이거나 탈퇴한 닉네임 입니다.'}, max_length=10, unique=True, verbose_name='닉네임')),
                ('profile_image', models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics', verbose_name='프로필 사진')),
                ('status', models.CharField(choices=[('N', 'user_normal'), ('S', 'user_stop'), ('W', 'user_withdrawal'), ('AW', 'admin_withdrawal')], default='N', max_length=20, verbose_name='회원 상태')),
                ('is_admin', models.BooleanField(default=False, verbose_name='어드민')),
                ('retention_period', models.TextField(choices=[('2023-11-23', '1year')], default='2023-11-23', verbose_name='회원정보 보유기간')),
                ('lock_count', models.IntegerField(default=0, verbose_name='로그인 제한 횟수')),
                ('lock_time', models.DateTimeField(null=True, verbose_name='로그인 제한 시간')),
                ('point', models.PositiveIntegerField(default=10000, verbose_name='포인트')),
                ('today_point', models.BooleanField(default=False, verbose_name='오늘 포인트받은 여부')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
