DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-byzwr3*z(xaiyki9+3&z#m9f&)n_fhgrt66e&bz9w^d=6-v0os'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postagram_api',
        'USER': 'postagram_api_user',
        'PASSWORD': 'taUbXnkNVaJPbnE4eHzLQOUIUFgA1Api',
        'HOST': 'dpg-cr6u8oi3esus7393ftr0-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}
