"""
Django settings for blog_api project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import datetime
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 添加导包路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3*78yt*3_s#_mf(s81tseait-5ky421ga9wvz)*0=n(4jhug(d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 第三方APP
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "drf_yasg",
    # 应用APP
    "settings",
    "user",
    "article",
    "category",
    "tag",
    "annual_summary",
    "friendlink",
    "photowall",
    "siteinfo"
]
# JWT配置
SIMPLE_JWT = {
    'TOKEN_EXPIRES': (60 * (60 * 1000)) * 24 * 5,
    # token有效时长
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=5),
    # token刷新后的有效时间
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
    # 自定义token返回的数据
    "TOKEN_OBTAIN_SERIALIZER": "user.serializer.CustomTokenObtainPairSerializer"
}
# 配置 rest_framework
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'EXCEPTION_HANDLER': 'blog_api.middleware.exception.custom_exception_handler'
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "blog_api.middleware.exception.ExceptionHandlerMiddleware",
    "blog_api.middleware.response.ResultMiddleware"
]

ROOT_URLCONF = "blog_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blog_api.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "blog",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "cheng20011101",
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'
            , 'charset': 'utf8mb4'}

    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# DENY ：表示该页面不允许在 frame 中展示，即便是在相同域名的页面中嵌套也不允许
# SAMEORIGIN ：表示该页面可以在相同域名页面的 frame 中展示
# ALLOW-FROM uri ：表示该页面可以在指定来源的 frame 中展示 (测试阶段使用)
X_FRAME_OPTIONS = "ALLOW-FROM"

# 允许跨域的地址,测试使用，线上建议关闭
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

# 博客设置
BLOG_SETTINGS = {
    # 前台网页设置
    "FRONT_SETTING": {
        "WEBSITE_TITLE": "",
        "WEBSITE_COVER": "",
        "RECORD_INFO": "",
        "COPYRIGHT": "",
        "CATEGORY": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
            "VISIBLE_MAX_NUM": 4
        },
        "TAGS": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
            "QUOTE_MAX_NUM": 4
        },
        "BLOG": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
            "RECOMMEND_MAX_NUM": 4
        }
    },
    # 后台台网页设置
    "ADMIN_SETTING": {
        "WEBSITE_TITLE": "",
        "WEBSITE_LOGO": "",
        "CATEGORY": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
        },
        "TAGS": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
        },
        "BLOG": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
        },
        "FRIEND_LINK": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
        },
        "PHOTO_WALL": {
            "PAGE_SIZE": 1,
            "MAX_PAGE_SIZE": 5,
        }
    },
    # 通用设置
    "COMMON_SETTING": {
        "HOME_DISPLAY": 4
    },
}

# 管理员信息设置
SUPER_USER_SETTINGS = {
    "nickname": "系统管理员",
    "signature": "因为没有个性，所以没有签名",
    "hobby": [
        {
            "name": "运动",
            "detail": "我爱运动"
        },
        {
            "name": "音乐",
            "detail": "我爱音乐"
        },
        {
            "name": "美术",
            "detail": "我爱美术"
        },
    ],
    "media": {
        "github": "Null",
        "bilibili": "Null",
        "csdn": "Null",
        "tiktok": "Null",
    }
}
