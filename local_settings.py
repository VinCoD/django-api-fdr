DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-byzwr3*z(xaiyki9+3&z#m9f&)n_fhgrt66e&bz9w^d=6-v0os'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'approved_project',
        'USER': 'approved_project_user',
        'PASSWORD': 'Qvgpl0x11JIUZwhFq0BjVeR4z0rAYbJQ',
        'HOST': 'dpg-cr53so52ng1s73eajicg-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}
